/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package taarea07restaurante;

/**
 *
 * @author milio
 */
public abstract class Empleado extends Persona {
    private int sueldoBase;

    public Empleado(String NIF, String nombre, String apellidos, int sueldoBase) {
        super(NIF, nombre, apellidos);
        this.sueldoBase = sueldoBase;
    }

    public int getSueldoBase() {
        return sueldoBase;
    }

    public void setSueldoBase(int sueldoBase) {
        this.sueldoBase = sueldoBase;
    }

    public abstract int calcularSueldo();
}
