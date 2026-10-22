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
public class Cocinero extends Empleado {
    private String turno;
    private int comision;
    private double menus;

    public Cocinero(String NIF, String nombre, String apellidos, int sueldoBase, String turno, int comision) {
        super(NIF, nombre, apellidos, sueldoBase);
        this.turno = turno;
        this.comision = comision;
        this.menus = 0;
    }

    public String getTurno() {
        return turno;
    }

    public void setTurno(String turno) {
        this.turno = turno;
    }

    public int getComision() {
        return comision;
    }

    public void setComision(int comision) {
        this.comision = comision;
    }

    public double getMenus() {
        return menus;
    }

    public void setMenus(double menus) {
        this.menus = menus;
    }

    @Override
    public int calcularSueldo() {
        return (int) (((comision * menus) / 100) + getSueldoBase());
    }
}
