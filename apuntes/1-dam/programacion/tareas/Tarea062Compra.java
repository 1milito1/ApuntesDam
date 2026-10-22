/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea062compra;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

/**
 *
 * @author milio
 */
public class Tarea062Compra {

    /**
     * @param args the command line arguments
     */    
    private static final String FICHERO_DATOS = "datos.dat";
    private static Map<String, Articulo> almacenamiento;

    public static void main(String[] args) {
        cargarAlmacenamiento();
        
        Scanner scanner = new Scanner(System.in);
        int opcion;
        
        do {            
            mostrarMenu();
            opcion = scanner.nextInt();
            
            switch (opcion) {
                case 1:
                    agregarArticulo(scanner);
                    break;
                case 2:
                    listarArticulos();
                    break;
                case 3:
                    borrarArticulo(scanner);
                    break;
                case 4:
                    modificarArticulo(scanner);
                    break;
                case 5:
                    guardarAlmacenamiento();
                    System.out.println("Saliendo de la aplicación...");
                    break;
                default:
                    System.out.println("Opción no válida");
            }
        } while (opcion!=5);      
              
    }
    
    private static void cargarAlmacenamiento(){
        try {
            FileInputStream fis = new FileInputStream(FICHERO_DATOS);
            ObjectInputStream ois = new ObjectInputStream (fis);
            almacenamiento = (Map<String, Articulo>) ois.readObject();
            ois.close();
        } catch (IOException | ClassNotFoundException e) {
            almacenamiento = new TreeMap<>();
        }
    }
    
    private static void guardarAlmacenamiento(){
        try {
            FileOutputStream fos = new FileOutputStream(FICHERO_DATOS);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(almacenamiento);
            oos.close();
        } catch (IOException e) {
            System.out.println("Error al guardar el almacenamiento");
        }
    }
    
    private static void agregarArticulo(Scanner scanner){
        System.out.print("Ingrese el código del artículo(6 catacteres alfanuméricos): ");
        String codigo = scanner.next();
        System.out.print("Ingrese la denominación del articulo: ");
        String denominacion = scanner.next();
        System.out.print("Ingrese el numero de unidades: ");
        int unidades = scanner.nextInt();
        System.out.print("Ingrese el precio del articulo: ");
        double precio = scanner.nextDouble();
        
        if(almacenamiento.containsKey(codigo)){
            System.out.println("El artículo ya existe. ¿Desesa actualizar el número de unidades s/n?");
            char respuesta = scanner.next().charAt(0);
            if (respuesta == 's'){
                Articulo articulo = almacenamiento.get(codigo);
                articulo.setUnidades(unidades);
            }else {
                System.out.println("No se ha agregado el artículo");
            }
        }else {
            Articulo articulo = new Articulo(denominacion, unidades, precio, codigo);
            almacenamiento.put(codigo, articulo);
            System.out.println("Artículo agregado correctamente");
        }
        
    }
    
    private static void listarArticulos(){
        double importeTotal = 0;
        for (Articulo articulo : almacenamiento.values()){
            System.out.println(articulo.toString());
            importeTotal += articulo.getPrecio() * articulo.getUnidades();
        }
        System.out.println("Importe total: " + importeTotal);
    }
    
    private static void borrarArticulo(Scanner scanner){
        System.out.print("Ingrese el codigo del artículo a borrar: ");
        String codigo = scanner.next();
        if(almacenamiento.containsKey(codigo)){
            almacenamiento.remove(codigo);
            System.out.println("Artículo borrado correctamente");
        }else{
            System.out.println("No se encontró el artículo con el código ingresado");
        }
    }
    
    private static void modificarArticulo(Scanner scanner){
        System.out.print("Ingrese el código del artículo a modificar: ");
        String codigo = scanner.next();
        if(almacenamiento.containsKey(codigo)){
            Articulo articulo = almacenamiento.get(codigo);
            System.out.print("Ingrese la nueva denominación del artículo: ");
            String denominacion = scanner.next();
            System.out.print("Ingrese el nuevo número de unidades: ");
            int unidades = scanner.nextInt();
            System.out.print("Ingrese el nuevo precio del artículo: ");
            double precio = scanner.nextDouble();
            
            articulo.setDenominacion(denominacion);
            articulo.setUnidades(unidades);
            articulo.setPrecio(precio);
            
            System.out.println("Articulo modificado correctamente");
        }else{
            System.out.println("No se encontró el artículo con el código ingresado.");
        }
    }
    
    private static void mostrarMenu(){
        System.out.println("Seleccione una opción: ");
        System.out.println("1. Agregar artículo");
        System.out.println("2. Listar articulo");
        System.out.println("3. Borrar artículo");
        System.out.println("4. Modificar artículo");
        System.out.println("5. Salir");
    }
}
