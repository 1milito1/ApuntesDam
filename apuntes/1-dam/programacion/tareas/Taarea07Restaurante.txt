/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package taarea07restaurante;

import java.util.Scanner;

/**
 *
 * @author milio
 */
public class Taarea07Restaurante {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
      
        Scanner scanner = new Scanner(System.in);
        Restaurante restaurante = new Restaurante();
        int opcion;
        
        do {
              System.out.println("Menú de operaciones:");
            System.out.println("1. Añadir empleado.");
            System.out.println("2. Listar.");
            System.out.println("3. Buscar.");
            System.out.println("4. Añadir trabajo.");
            System.out.println("5. Añadir cocinado.");
            System.out.println("6. Calcular sueldo.");
            System.out.println("7. Salir.");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine();
            
            switch (opcion) {
                case 1:
                    System.out.println("Añadir el NIF: ");
                    String NIF = scanner.nextLine();
                    System.out.println("Añadir el nombre: ");
                    String nombre = scanner.nextLine();
                    System.out.println("Añadir el apellido: ");
                    String apellido = scanner.nextLine();
                    System.out.println("Añadir el sueldo base: ");
                    int sueldoBase = scanner.nextInt();
                    scanner.nextLine();
                    System.out.println("Introduzca el tipo de empleado Camarero/Cocinero: ");
                    String tipoEmpleado = scanner.nextLine();
                    if (tipoEmpleado.equalsIgnoreCase("camarero")){
                        System.out.println("Introduzca el precio por hora: ");
                        int precioHora = scanner.nextInt();
                        restaurante.añadirEmpleado(NIF, nombre, apellido, sueldoBase, tipoEmpleado, precioHora, " ", 0);
                    }else if (tipoEmpleado.equalsIgnoreCase("cocinero")){
                        System.out.println("Introduzca el turno mañana/tarde: ");
                        String turno = scanner.nextLine();
                        System.out.println("Introduzca la comision (%): ");
                        int comision = scanner.nextInt();
                        restaurante.añadirEmpleado(NIF, nombre, apellido, sueldoBase, tipoEmpleado, opcion, turno, comision);
                    }else{
                        System.out.println("Tipo de empleado no válido.");
                    }
                  break;
                case 2:
                    System.out.println("Listado de empleados: ");
                    restaurante.listar();
                    break;
                case 3:
                    System.out.println("Buscar empleado:");
                    System.out.println("Introduzca el NIF: ");
                    String nifBusqueda = scanner.nextLine();
                    Empleado empleadoBuscado = restaurante.buscaEmpleado(nifBusqueda);
                    if (empleadoBuscado != null){
                        System.out.println("Empleado encontrado: ");
                        System.out.println(empleadoBuscado);
                    }else{
                        System.out.println("Empleado no encontrado.");
                    }
                    break;
                case 4:
                     System.out.print("Introduzca el NIF del camarero: ");
                    String nifCamarero = scanner.nextLine();
                    System.out.print("Introduzca las horas trabajadas: ");
                    int horasTrabajadas = scanner.nextInt();
                    restaurante.añadirTrabajo(nifCamarero, horasTrabajadas);
                    break;
                case 5:
                    System.out.print("Introduzca el NIF del cocinero: ");
                    String nifCocinero = scanner.nextLine();
                    restaurante.añadirMenu(nifCocinero);
                    break;
                case 6:
                    System.out.print("Introduzca el NIF del empleado: ");
                    String nifSueldo = scanner.nextLine();
                    restaurante.calcularSueldo(nifSueldo);
                    break;
                case 7:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción no válida. Por favor, seleccione una opción del menú.");
                    break;
            }
        } while (opcion != 7);
    }
}
