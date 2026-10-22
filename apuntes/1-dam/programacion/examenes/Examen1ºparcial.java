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
public class Examen1ºparcial {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
       Almacen almacen = new Almacen();
       
       Producto producto1 = new Producto("123abc", "oro", 10, 5.4, false);
       Producto producto2 = new Producto("456def", "plata", 5, 3.3, false);
       Producto producto3 = new Producto("789ghi", "bronce", 2, 1.3, false);
       
       almacen.añadirProducto(producto1);
       almacen.añadirProducto(producto2);
       almacen.añadirProducto(producto3);
       
       Producto productoBuscado = almacen.buscarProducto("123abc");
        if (productoBuscado != null) {
            System.out.println("Producto encontrado: " + productoBuscado);
        } else {
            System.out.println("Producto no encontrado.");
        }
        
        // Calcular el inventario total del almacén
        double inventarioTotal = almacen.calcularInventarioTotal();
        System.out.println("Valor total del inventario del almacén: " + inventarioTotal);
        
        // Mostrar todos los productos del almacén
        System.out.println("Listado de productos en el almacén:");
        System.out.println(almacen);
        
        
        MenuProducto menuProducto = new MenuProducto();
        menuProducto.mostrarMenu();3
                
    }
}