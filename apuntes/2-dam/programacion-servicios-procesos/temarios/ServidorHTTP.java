package org.example;


import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ServidorHTTP {

    private static final int PUERTO = 8066; // Define el puerto en el que se conecta el servidor a la escucha


    public static void main(String[] args) {

        try (ServerSocket servidorSocket = new ServerSocket(PUERTO)){ //Crea un ServerSocket que escucha el puerto especificado
            System.out.println("Servidor HTTP escuchando en el puerto " + PUERTO);

            while (true){ //Bucle infinito para aceptar conexiones de clientes
                Socket clienteSocket = servidorSocket.accept(); //Acepta una conexion
                System.out.println("Cliente conectado desde: " + clienteSocket.getInetAddress().getHostAddress());

                // Crea un nuevo hilo para manejar la conexión del cliente
                Thread hiloCliente = new Thread(new ManejadorClente(clienteSocket));
                hiloCliente.start(); // Inicia el hilo, lo que ejecuta el método run del ManejadorCliente
            }

        }catch (IOException e){
            System.err.println("Error al iniciar el servidor: " + e.getMessage());
        }
    }
}