package org.example;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.*;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.concurrent.ConcurrentLinkedDeque;
import java.util.concurrent.ConcurrentHashMap;

public class ServidorPedidos {

    private static final int PUERTO = 12345;
    private static final String ARCHIVO_STOCK = "config_stock.properties";
    private static final String LOG_FILE = "pedidos.log";

    private static final Map<String, Integer> stock = new ConcurrentHashMap<>();
    private static final Queue<String[]> colaPedidos = new ConcurrentLinkedDeque<>();
    private static int numeroPedido = 1; // Contador para asignar una ID a los pedidos.

    public static void main(String[] args) {
        cargarStock(); //Carga el stock inicial desde el archivo de configuracion
        monitorearStock(); // Inicia la monitorización de cambios en el archivo de stock
        new Thread(ServidorPedidos::procesarPedidos).start(); // Inicia el procesamiento
        iniciarConexiones(); // Inicia el servidor de pedidos
    }

    // Inicia el servidor y espera las conexiones de los almacenes (clientes)

    private static void iniciarConexiones(){
        System.out.println("Servidor de pedidos iniciado en el puerto " + PUERTO);

        try (ServerSocket serverSocket = new ServerSocket(PUERTO)) {
            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Almacén conectado desde: " + socket.getInetAddress().getHostAddress());
                new Thread(() -> manejarCliente(socket)).start();
            }
        } catch (IOException e) {
            System.err.println("Error en el servidor: " + e.getMessage());
        }
    }


    //Maneja la comunicación con un almacén que realiza pedidos

    private static void manejarCliente(Socket socket) {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {

            String almacen = socket.getInetAddress().getHostAddress();
            String linea;
            while ((linea = in.readLine()) != null) {
                String[] pedidoDatos = linea.split(",");
                if (pedidoDatos.length != 2) {
                    out.println("Formato inválido. Use: producto,cantidad");
                    continue;
                }
                String producto = pedidoDatos[0].trim();
                int cantidad;
                try {
                    cantidad = Integer.parseInt(pedidoDatos[1].trim());
                } catch (NumberFormatException e) {
                    out.println("Cantidad inválida.");
                    continue;
                }
                int pedidoID;
                synchronized (ServidorPedidos.class){
                    pedidoID = numeroPedido++;
                }

                colaPedidos.add(new String[]{almacen, producto, String.valueOf(cantidad), String.valueOf(pedidoID)});
                out.println("Pedido recibido: " + pedidoID + " - Producto: " + producto + " - Cantidad: " + cantidad);
            }
        } catch (IOException e) {
            System.err.println("Error en la conexión con el almacén: " + e.getMessage());
        }
    }

    // Procesa los pedidos en cola de manera secuencial

    private static void procesarPedidos() {
        while (true) {
            String[] pedidoDatos = colaPedidos.poll();
            if (pedidoDatos != null) {
                procesarPedido(pedidoDatos[0], pedidoDatos[1], Integer.parseInt(pedidoDatos[2]), Integer.parseInt(pedidoDatos[3]));
            } else {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    System.err.println("Hilo procesador interrumpido");
                }
            }
        }
    }

    // Procesa un pedido verificando la disponibilidad de stock y registrándolo.

    private static void procesarPedido(String almacen, String producto, int cantidad, int pedidoID) {
        boolean aceptado;
        synchronized (stock) {
            int stockActual = stock.getOrDefault(producto, 0);
            aceptado = stockActual >= cantidad;
            if (aceptado) {
                stock.put(producto, stockActual - cantidad);
            }
        }
        registrarPedido(almacen, producto, cantidad, pedidoID, aceptado);
    }

    //Registra un pedido en el log

    private static void registrarPedido(String almacen, String producto, int cantidad, int pedidoID, boolean aceptado) {
        String estado = aceptado ? "ACEPTADO" : "RECHAZADO (Stock insuficiente)";
        String logMensaje = String.format("[%s] PEDIDO %d - Almacén: %s - Producto: %s - Cantidad: %d - %s",
                new SimpleDateFormat("dd-MM-yyyy HH:mm:ss").format(new Date()), pedidoID, almacen, producto, cantidad, estado);

        System.out.println(logMensaje);

        try (FileWriter fw = new FileWriter(LOG_FILE, true);
             BufferedWriter bw = new BufferedWriter(fw)) {
            bw.write(logMensaje);
            bw.newLine();
        } catch (IOException e) {
            System.err.println("Error al escribir en el log: " + e.getMessage());
        }
    }

    //Carga el stock inicial desde el archivo de configuración

    private static void cargarStock() {
        Properties propiedades = new Properties();
        try (FileInputStream fis = new FileInputStream(ARCHIVO_STOCK)) {
            propiedades.load(fis);
            for (String producto : propiedades.stringPropertyNames()) {
                stock.put(producto, Integer.parseInt(propiedades.getProperty(producto)));
            }
            System.out.println("Stock cargado correctamente.");
        } catch (IOException | NumberFormatException e) {
            System.err.println("Error cargando el stock: " + e.getMessage());
        }
    }

    //Monitorea los cambios en el archivo de stock y lo recarga automáticamente si este cambia.
    private static void monitorearStock() {
        new Thread(() -> {
            try {
                WatchService watchService = FileSystems.getDefault().newWatchService();
                Path path = Paths.get(ARCHIVO_STOCK).toAbsolutePath().getParent();
                if (path == null) path = Paths.get(".").toAbsolutePath();
                path.register(watchService, StandardWatchEventKinds.ENTRY_MODIFY);

                while (true) {
                    WatchKey key = watchService.take();
                    for (WatchEvent<?> event : key.pollEvents()) {
                        if (event.context().toString().equals(ARCHIVO_STOCK)) {
                            System.out.println("Archivo de stock modificado. Recargando...");
                            Thread.sleep(500);
                            cargarStock();
                        }
                    }
                    key.reset();
                }
            } catch (Exception e) {
                System.err.println("Error en la monitorización del stock: " + e.getMessage());
            }
        }).start();
    }
}
