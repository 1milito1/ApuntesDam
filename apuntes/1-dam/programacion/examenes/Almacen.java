/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package examen1ºparcial;

import java.util.HashSet;
import java.util.Set;

/**
 *
 * @author milio
 */
public class Almacen {
    private Set<Producto> almacen;
    
    public Almacen(){
        almacen = new HashSet<>();
        
    }
    
    public void añadirProducto(Producto producto){
        if (almacen.add(producto)){
            System.out.println("Producto añadido");
        }else{
            System.out.println("producto ya existe");
        }
        
    }
    
    public Producto buscarProducto (String cod_producto){
        for (Producto producto : almacen){
            if (producto.getCod_producto().equals(cod_producto)){
            return (producto);
        }
        }
        return null;
    }
    
    public double calcularInventarioTotal(){
        double total = 0;
        for (Producto producto : almacen){
            total += producto.calcularInventario();
        }
        return total;
    }

    @Override
    public String toString() {
        return "Almacen{" + "almacen=" + almacen + '}';
    }
    
}
