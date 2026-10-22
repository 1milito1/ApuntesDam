package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Random;
import java.util.concurrent.TimeUnit;

public class ClienteAlmacen {

    private static final String SERVER_IP = "127.0.0.1";
    private static final int SERVER_PORT = 12345;
    private static final String[] PRODUCTOS = {"producto1", "producto2", "producto3", "producto4", "producto5"};

    public static void main(String[] args) {

        try (Socket socket = new Socket(SERVER_IP, SERVER_PORT);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))){

            System.out.println("Conectado al servidor de pedidos.");

            Random random = new Random();

            while (true){
            String producto = PRODUCTOS[random.nextInt(PRODUCTOS.length)]; // Selecciona un producto aleatorio
            int cantidad = random.nextInt(20) + 1; // genera una cantidad aleatoria entre 1 y 20

            out.println(producto + "," + cantidad); // Envía el pedido al servidor
                System.out.println("Pedido enviado: " + producto + ", cantidad: " + cantidad);


            String respuesta = in.readLine(); //Recibe la respuesta del servidor
                System.out.println("Respuesta del servidor: " +  respuesta);

                TimeUnit.SECONDS.sleep(random.nextInt(6) + 5); // espera entre 5 y 10 segundos antes de enviar otro pedido
            }

        }catch (IOException | InterruptedException e){
            e.printStackTrace();
        }
    }
}
