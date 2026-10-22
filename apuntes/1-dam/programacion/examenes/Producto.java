/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package examen1ºparcial;

/**
 *
 * @author milio
 */
public class Producto {
    
   private String cod_producto;
   private String nombre;
   private int unidades;
   private double precio;
   private boolean devolucion;

    
    public String getCod_producto() {
        return cod_producto;
    }

    public void setCod_producto(String cod_producto) {
        this.cod_producto = cod_producto;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getUnidades() {
        return unidades;
    }

    public void setUnidades(int unidades) {
        this.unidades = unidades;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public boolean isDevolucion() {
        return devolucion;
    }

    public void setDevolucion(boolean devolucion) {
        this.devolucion = devolucion;
    }

    public Producto(String cod_producto, String nombre, int unidades, double precio, boolean devolucion) {
        this.cod_producto = cod_producto;
        this.nombre = nombre;
        this.unidades = unidades;
        this.precio = precio;
        this.devolucion = devolucion;
    }

    @Override
    public String toString() {
        return "Producto{" + "cod_producto=" + cod_producto + ", nombre=" + nombre + ", unidades=" + unidades + ", precio=" + precio + ", devolucion=" + devolucion + '}';
    }
   
   
   public double calcularInventario(){
       return unidades * precio;
   }
}

