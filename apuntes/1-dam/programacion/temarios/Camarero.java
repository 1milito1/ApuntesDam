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
public class Camarero extends Empleado {
    private int precioHora;
    private int horasTrabajadas;

    public Camarero(String NIF, String nombre, String apellidos, int sueldoBase, int precioHora) {
        super(NIF, nombre, apellidos, sueldoBase);
        this.precioHora = precioHora;
        this.horasTrabajadas = 0;
    }

    public int getPrecioHora() {
        return precioHora;
    }

    public void setPrecioHora(int precioHora) {
        this.precioHora = precioHora;
    }

    public int getHorasTrabajadas() {
        return horasTrabajadas;
    }

    public void setHorasTrabajadas(int horasTrabajadas) {
        this.horasTrabajadas = horasTrabajadas;
    }

    @Override
    public int calcularSueldo() {
        return (horasTrabajadas * precioHora) + getSueldoBase();
    }
}
