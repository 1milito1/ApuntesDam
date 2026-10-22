package org.example;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.*;


public class Main {

    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    static {
        try {
            FileHandler fileHandler = new FileHandler("app_log.txt", true);
            SimpleFormatter formatter = new SimpleFormatter();
            fileHandler.setFormatter(formatter);
            LOGGER.addHandler(fileHandler);
            ConsoleHandler consoleHandler = new ConsoleHandler();
            consoleHandler.setFormatter(formatter);
            LOGGER.addHandler(consoleHandler);
            LOGGER.setLevel(Level.INFO);
            LOGGER.info("Aplicación iniciada.");
        }catch (IOException e){
            LOGGER.log(Level.SEVERE, "Error al configurar el logger", e);
        }
    }

    private static void validarLogin(BufferedReader reader) throws IOException{
        String login;
        while (true){
            System.out.println("Introduce tu login (8 caracteres, solo minúsculas): ");
            login = reader.readLine();
            if (login == null ||login.length() != 8 || !login.matches("[a-z]{8}")){
                LOGGER.warning("Intento de login inválido: " + login);
                System.out.println("Login inválido. debe tener 8 caracteres y coentener sólo minúsculas");
            }else {
                LOGGER.info("Login introducido: " + login);
                break;
            }
        }
    }

    private static String validarNombreFichero (BufferedReader reader) throws IOException{
        String nombreFichero;
        while (true){
            System.out.println("Introduce el nombre del fichero a mostrar (máximo 8 caracteres más la extensión): ");
            nombreFichero = reader.readLine();
            if (nombreFichero == null || nombreFichero.length() > 12 || !nombreFichero.matches("[a-zA-Z0-9]+\\.[a-zA-Z0-9]{3}")){
                LOGGER.warning("Itento de nombre de fichero inválido: " + nombreFichero);
                System.out.println("Nombre de fichero inválido. Debe tener como máximo 8 caracteres más una extensión de 3.");

            }else {
                LOGGER.info("Nombre de fichero introducido: " + nombreFichero);
                break;
            }
        }
        return nombreFichero;
    }

    private static void visualizarFichero(String nombreFichero){
        try (BufferedReader fileReader = new BufferedReader(new FileReader(nombreFichero))){
            System.out.println("\nContenido del fichero '" + nombreFichero + "':");
            String linea;
            while ((linea = fileReader.readLine()) !=null){
                System.out.println(linea);
            }
            LOGGER.info("Fichero '" + nombreFichero + "' visualizado correctamente.");

        }catch (IOException e){
            LOGGER.log(Level.SEVERE, "Error al leer el fichero '" + nombreFichero + "'", e);
            System.out.println("Error al leer el fichero: " + e.getMessage());
        }
    }

    public static void main(String[] args) {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            validarLogin(reader);
            String nombreFichero = validarNombreFichero(reader);
            visualizarFichero(nombreFichero);
        }catch (IOException e){
            LOGGER.log(Level.SEVERE, "Error de entrada/salida", e);
            System.err.println("Error de entrada/salida: " + e.getMessage());
        }finally {
            try {
                reader.close();
            }catch (IOException e){
                LOGGER.log(Level.WARNING, "Error al cerrar el lector", e);
            }
            LOGGER.info("Aplicación finalizada.");
        }
    }
}