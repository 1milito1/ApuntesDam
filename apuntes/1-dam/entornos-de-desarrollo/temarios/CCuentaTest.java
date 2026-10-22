/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package prácticaunidad3;

import junit.framework.TestCase;

/**
 *
 * @author milio
 */
public class CCuentaTest extends TestCase {
    
    public CCuentaTest(String testName) {
        super(testName);
    }
 
    /**
     * Test of asignarNombre method, of class CCuenta.
     */
    public void testAsignarNombre() {
        System.out.println("asignarNombre");
        String nom = "";
        CCuenta instance = new CCuenta();
        instance.asignarNombre(nom);
       
    }

    /**
     * Test of obtenerNombre method, of class CCuenta.
     */
    public void testObtenerNombre() {
        System.out.println("obtenerNombre");
        CCuenta instance = new CCuenta();
        String expResult = "Juan";
        String result = instance.obtenerNombre();
        assertEquals(expResult, result, null);
        
    }

    /**
     * Test of estado method, of class CCuenta.
     */
    public void testEstado() {
        System.out.println("estado");
        CCuenta instance = new CCuenta();
        double expResult = 3000.0;
        double result = instance.estado();
        assertEquals(expResult, result, 0.0);
        System.out.println ("Estado cuenta"+ instance.estado());
        
    }

    /**
     * Test of ingresar method, of class CCuenta.
     */
    public void testIngresar() throws Exception {
      
        double cantidad = 500.0;
        CCuenta instance = new CCuenta();
        instance.ingresar(cantidad);
          System.out.println("ingresar"+ cantidad);
    }

    /**
     * Test of retirar method, of class CCuenta.
     */
    public void testRetirar() throws Exception {
        
        double cantidad = 1000.0;
        CCuenta instance = new CCuenta();
        instance.retirar(cantidad);
        System.out.println("retirar"+ cantidad);
    }

    /**
     * Test of obtenerCuenta method, of class CCuenta.
     */
    public void testObtenerCuenta() {
        System.out.println("obtenerCuenta");
        CCuenta instance = new CCuenta();
        String expResult = "12345";
        String result = instance.obtenerCuenta();
        assertEquals(expResult, result,null);
        
    }
    
    public void testingresarYretirar() throws Exception {
        CCuenta instance = new CCuenta();
        double cantidadIngresar = 1500.0;
        double cantidadRetirar = 1000.0;
        instance.ingresar(cantidadIngresar);
        instance.retirar(cantidadRetirar);
        System.out.println("Ingresar"+ cantidadIngresar); 
        System.out.println("Retirar"+ cantidadRetirar);
        System.out.println("El total de la cuenta después de ingresar y retirar al mismo tiempo es" + instance.estado());
    }
   

    
}
