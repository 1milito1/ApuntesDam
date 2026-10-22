
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author milio
 */


public class CoordinarProcesos {
    public static void main(String[] args) {
        // Verificar que se han pasado los argumentos necesarios
        if (args.length != 3) {
            System.out.println("Uso: java -jar coordinarProcesos.jar <entrada.txt> <numInstancias> <salida_final.txt>");
            return;
        }

        String archivoEntrada = args[0];
        int numInstancias = Integer.parseInt(args[1]);
        String archivoSalidaFinal = args[2];

        // Dividir el archivo de entrada en partes
        List<String> archivosTemporales = dividirArchivo(archivoEntrada, numInstancias);

        // Lanzar instancias de ProcesarPalabras
        List<Process> procesos = new ArrayList<>();
        for (String archivoTemporal : archivosTemporales) {
            try {
                ProcessBuilder pb = new ProcessBuilder("java", "-jar", "ProcesarPalabras.jar", archivoTemporal, archivoTemporal + "_salida.txt");
                procesos.add(pb.start());
            } catch (IOException e) {
                System.err.println("Error al iniciar el proceso: " + e.getMessage());
            }
        }

        // Esperar a que todos los procesos terminen
        for (Process proceso : procesos) {
            try {
                proceso.waitFor();
            } catch (InterruptedException e) {
                System.err.println("Error al esperar el proceso: " + e.getMessage());
            }
        }

        // Combinar los archivos de salida en el archivo final
        combinarArchivos(archivosTemporales, archivoSalidaFinal);
        
        // Limpiar archivos temporales
        for (String archivoTemporal : archivosTemporales) {
            new File(archivoTemporal).delete();
            new File(archivoTemporal + "_salida.txt").delete();
        }
    }

    private static List<String> dividirArchivo(String archivoEntrada, int numInstancias) {
        List<String> archivosTemporales = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(archivoEntrada))) {
            String linea;
            int contador = 0;
            int instancia = 0;
            BufferedWriter bw = null;

            while ((linea = br.readLine()) != null) {
                if (contador % (numInstancias + 1) == 0) {
                    if (bw != null) {
                        bw.close();
                    }
                    instancia++;
                    String archivoTemporal = "temp_" + instancia + ".txt";
                    archivosTemporales.add(archivoTemporal);
                    bw = new BufferedWriter(new FileWriter(archivoTemporal));
                }
                bw.write(linea);
                bw.newLine();
                contador++;
            }
            if (bw != null) {
                bw.close();
            }
        } catch (IOException e) {
            System.err.println("Error al dividir el archivo: " + e.getMessage());
        }
        return archivosTemporales;
    }

    private static void combinarArchivos(List<String> archivosTemporales, String archivoSalidaFinal) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(archivoSalidaFinal))) {
            for (String archivoTemporal : archivosTemporales) {
                try (BufferedReader br = new BufferedReader(new FileReader(archivoTemporal + "_salida.txt"))) {
                    String linea;
                    while ((linea = br.readLine()) != null) {
                        bw.write(linea);
                        bw.newLine();
                    }
                }
            }
        } catch (IOException e) {
            System.err.println("Error al combinar los archivos: " + e.getMessage());
        }
    }
}