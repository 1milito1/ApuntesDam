/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea02ejercicio05;

/**
 *
 * @author milio
 */
import java.util.Scanner;

public class Tarea02Ejercicio05 {

    /**
     * @param args the command line arguments
     */
   public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        System.out.print("Ingrese el nombre del electrodoméstico: ");
        String nombreElectrodomestico = scanner.nextLine();

        System.out.print("Ingrese el precio del electrodoméstico en €: ");
        double precioElectrodomestico = scanner.nextDouble();

       
        double interesInicial = 0.025; 
        double interesActual = interesInicial;
        double cuotaMensual = 100.0;
        double totalAPagar = 0.0;

        System.out.println("\nDetalles del financiamiento para " + nombreElectrodomestico + ":");
        for (int cuota = 1; cuota <= 3; cuota++) {
            double interes = precioElectrodomestico * interesActual;
            cuotaMensual += interes;
            totalAPagar += cuotaMensual;

            System.out.printf("Cuota %d: %.2f €\n", cuota, cuotaMensual);
            
            
            interesActual *= 2;
        }

        System.out.printf("\nEl total a pagar es: %.2f €\n", totalAPagar);
    }
}