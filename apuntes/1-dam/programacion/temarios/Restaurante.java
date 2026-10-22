/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package taarea07restaurante;

import java.util.ArrayList;

/**
 *
 * @author milio
 */
public class Restaurante {
    private ArrayList<Empleado> empleados;

    public Restaurante() {
        empleados = new ArrayList<>();
    }
    public void añadirEmpleado(String NIF, String nombre, String apellidos, int sueldoBase, String tipoEmpleado, int precioHora, String turno, int comision) {
        Empleado empleado;
        if (tipoEmpleado.equalsIgnoreCase("camarero")) {
            empleado = new Camarero(NIF, nombre, apellidos, sueldoBase, precioHora);
        } else {
            empleado = new Cocinero(NIF, nombre, apellidos, sueldoBase, turno, comision);
        }
    empleados.add(empleado);
}

    
    public Empleado buscaEmpleado(String NIF){
        for (Empleado empleado : empleados){
            if (empleado.getNIF().equals(NIF)){
                return empleado;
            }
        }
        return null;
    }
    
    public void listar(){
        empleados.sort((emp1, emp2) -> emp1.getApellidos().compareTo(emp2.getApellidos()));
        for (Empleado empleado : empleados){
            System.out.println(empleado);
        }
        
    }
    
    public void añadirTrabajo(String NIF, int horas){
        Empleado empleado = buscaEmpleado(NIF);
        if (empleado instanceof Camarero){
            ((Camarero) empleado).setHorasTrabajadas(((Camarero) empleado).getHorasTrabajadas() + horas);
        }
        
    }
    
    public void añadirMenu(String NIF){
       Empleado empleado = buscaEmpleado(NIF);
       if (empleado instanceof Cocinero){
           ((Cocinero) empleado).setMenus(((Cocinero) empleado).getMenus() + 1);
       }
        
    }
    
    public void calcularSueldo(String NIF) {
    Empleado empleado = buscaEmpleado(NIF);
    if (empleado != null) {
        if (empleado instanceof Camarero) {
            Camarero camarero = (Camarero) empleado;
            System.out.println("Sueldo de " + camarero.getNombre() + " " + camarero.getApellidos() + ": " + camarero.calcularSueldo());
        } else if (empleado instanceof Cocinero) {
            Cocinero cocinero = (Cocinero) empleado;
            System.out.println("Sueldo de " + cocinero.getNombre() + " " + cocinero.getApellidos() + ": " + cocinero.calcularSueldo());
        } else {
            System.out.println("Sueldo de " + empleado.getNombre() + " " + empleado.getApellidos() + ": " + empleado.calcularSueldo());
        }
    } else {
        System.out.println("Empleado no encontrado.");
    }
}

}
