
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author milio
 */
public class ProcesarPalabras {
    
    public static void main(String[] args){
        
        if (args.length != 2) {
            System.out.println("Uso: java -jar ProcesarPalabras.jar <entrada.txt> <salida.txt>");
            return;
        }
        String archivoEntrada = args[0];
        String archivoSalida = args[1];
        
        try (BufferedReader br = new BufferedReader (new FileReader(archivoEntrada));
             BufferedWriter bw = new BufferedWriter (new FileWriter(archivoSalida))){
            
            String linea;
            while ((linea = br.readLine()) != null) {
                
                String palabraTransformada = procesarPalabra(linea);
                bw.write(palabraTransformada);
                bw.newLine();
            }
        }catch (IOException e){
            System.err.println("Error al procesar los archivos: " + e.getMessage());
        }
    }
    
    private static String procesarPalabra (String palabra){
        if (palabra.length() % 2 == 0){
            return palabra.toUpperCase();
            
        }else {
            return palabra.toLowerCase();
        }
    }
    
}
