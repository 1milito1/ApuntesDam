/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package examen1ºparcial;

import java.util.Scanner;

/**
 *
 * @author milio
 */
public class MenuProducto {
    
    private Producto producto;
    private Scanner scanner;
    
    public MenuProducto(){
        scanner = new Scanner(System.in);
        
    }
    
    public void mostrarMenu(){
        int opcion;
        do {
            System.out.println("Menú Productos: ");
            System.out.println("1. Crear un producto: ");
            System.out.println("2. Modificar unidades del producto: ");
            System.out.println("3. Mostrar datos del producto: ");
            System.out.println("4. Calcular el inventario del producto: ");
            System.out.println("5. Salir.");
            System.out.println("Elije una opción");
         opcion = scanner.nextInt();
         scanner.nextLine();
            
            switch (opcion) {
                case 1:
                       crearProducto();                 
                    break;
                case 2:
                    modificarProducto();
                    break;
                case 3:
                    mostrarProducto();
                    break;
                case 4:
                    calcularProducto();
                    break;
                case 5:
                    System.out.println("Saliendo del menu...");
                    break;
                default:
                    System.out.println("Opción no validad...");
            }
            
        }while (opcion != 5);
    }

    private void crearProducto() {
        System.out.println("Ingresa el codigo del producto: ");
        String cod_producto = scanner.nextLine();
        System.out.println("Ingresa el nombre del producto: ");
        String nombre = scanner.nextLine();
        System.out.println("Introduzca las unidades del producto: ");
        int unidades = scanner.nextInt();
        System.out.println("Introduzca el percio del producto: ");
        double precio = scanner.nextDouble();
        System.out.println("Permite devolucion (true/false): ");
        boolean devolucion = scanner.nextBoolean();
        
        producto = new Producto(cod_producto, nombre, unidades, precio, devolucion);
        System.out.println("Producto creado.");
    }

    private void modificarProducto() {
        if (producto == null){
            System.out.println("Primero debe de crear el producto.");
            return;
        }
        System.out.println("Introduzca el codigo del producto: ");
        int unidades = scanner.nextInt();
        producto.setUnidades(unidades);
        System.out.println("Unidades cambiadas.");
        
    }

    private void mostrarProducto() {
        if (producto ==null){
            System.out.println("primero debe de crear el producto: ");
            return;
        }
        System.out.println(producto);
    }

    private void calcularProducto() {
        if (producto == null){
        System.out.println("primero debe de crear el producto.");
        return;
    }
    double inventario = producto.calcularInventario();
        System.out.println(inventario);
    }
}
