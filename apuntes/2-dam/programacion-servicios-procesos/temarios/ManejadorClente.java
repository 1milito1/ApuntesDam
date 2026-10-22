package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ManejadorClente implements Runnable{ //Implementa la interfaz Runnable para poder ejecutar en un hilo
    private Socket clienteSocket; // Almacena el socket del cliente con el que se esta conectando

    //Constructor, recibe el socket del cliente.
    public ManejadorClente(Socket socket){
        this.clienteSocket = socket;
    }
    @Override
    public void run() {
        try (
                BufferedReader entrada = new BufferedReader(new InputStreamReader(clienteSocket.getInputStream()));
                PrintWriter salida = new PrintWriter(clienteSocket.getOutputStream(), true)
        ){
            String lineaPeticion = entrada.readLine(); // Lee la primera linea de la petición del cliente
            if (lineaPeticion !=null && lineaPeticion.startsWith("GET ")){ // verifica que sea una peticón GET válida
                String ruta = obtenerRuta(lineaPeticion);// Obtiene la ruta de la petición del cliente
                System.out.println("Petición: " + lineaPeticion); // Imprime la peticion en la consola del servidor
                responder(salida, ruta); // llama al método respondera para enviar la respuesta al cliente
            } else if(lineaPeticion != null){ // si la petición no es un GET válido
                System.out.println("Petición no GET o inválida: " + lineaPeticion);
                responderError(salida); // llama al método responderError para enviar una respuesta de error.
            }

        }catch (IOException e){
            System.err.println("Error al manejar la conexión del cliente: " + e.getMessage());
        } finally { // Bloque finally para asegurar que el socket se cierre
            try {
                clienteSocket.close(); // cierra el socket
                System.out.println("Cliente desconectado: " + clienteSocket.getInetAddress().getHostAddress());
            }catch (IOException e){
                System.err.println("Error al cerrar el socket del cleinte: " + e.getMessage());
            }
        }
    }

    //Método para obetner la ruta de la petición HTTP
    private String obtenerRuta(String lineaPeticion) {
        String[] partes = lineaPeticion.split(" "); // Divide la petición en partes (método, ruta, protocolo, etc.)
        if (partes.length >1){
            return partes[1]; // Devuelve la segunda parte, que es la ruta
        }
        return "/"; // Devuelve "/" por defecto si no se encuentra la ruta
    }

    // Metodo para responder al cliente con el contenido HTML corrspondete a la ruta de la petición
    private void responder(PrintWriter salida, String ruta){
        String contenidoHTML = ""; // Inicia la variable para almacenar el contenido HTML
        String cabecera = Mensajes.CABECERA_OK; // Inicializa la cabecera con la cabecera de éxito

        switch (ruta){ // Usan un switch para determinar que contenido HTML enviar según la ruta
            case "/":
                contenidoHTML = Paginas.getPaginaBinevenida();
                break;
            case "/curiosidad":
                contenidoHTML = Paginas.getPaginaCuriosidad();
                break;
            case "/contacto":
                contenidoHTML = Paginas.getPaginaContacto();
                break;
            default:
                cabecera = Mensajes.CABECERA_NOT_FOUND; // Si la ruta no coincide, usa la cabecera de NOT FOUND de error
                contenidoHTML = Paginas.getPaginaNotFound(); // Obtiene la página de error 404
                break;
        }
        salida.print(cabecera + contenidoHTML);

    }

    //Método para responder con la página de error 404
    private void responderError(PrintWriter salida){
        salida.print(Mensajes.CABECERA_NOT_FOUND + Paginas.getPaginaNotFound());
    }
}
