/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea02ejercicio04;

/**
 *
 * @author milio
 */
import java.util.Scanner;
public class Tarea02Ejercicio04 {
 public static void main(String[] args) {
 Scanner teclado = new Scanner (System.in);
 String nombre;
 String apellidos;
 System.out.println("Escribe tu nombre");
 nombre=teclado.nextLine();
 System.out.println("Escribe tus apellidos");
 apellidos=teclado.nextLine();
 System.out.printf( "Hola " + nombre +" "+ apellidos + ", bienvenido al ciclo DAM online");
 String nombreCompleto=nombre.concat(" ").concat(apellidos);
 int tamañoNombre=nombreCompleto.length();
 System.out.printf( "\nLa longitud de tu nombre y apellidos es:%d", tamañoNombre );
 System.out.printf("\nTu apodo será¡ %s", nombre.substring(0,4).toUpperCase() );
 System.out.println();
 }
}
