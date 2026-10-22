/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea08telefonografico;

import java.util.HashSet;
import java.util.Set;

/**
 *
 * @author milio
 */


public class Telefono {
    private String numTelefono;
    private String modelo;
    private Set<String> llamadas;

    public Telefono(String numTelefono, String modelo) {
        this.numTelefono = numTelefono;
        this.modelo = modelo;
        this.llamadas = new HashSet<>();
    }

    public String getNumTelefono() {
        return numTelefono;
    }

    public void setNumTelefono(String numTelefono) {
        this.numTelefono = numTelefono;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public Set<String> getLlamadas() {
        return llamadas;
    }

    public void llamarA(String numero) {
        llamadas.add(numero);
    }

    @Override
    public String toString() {
        return "Telefono{" +
                "numTelefono='" + numTelefono + '\'' +
                ", modelo='" + modelo + '\'' +
                ", llamadas=" + llamadas +
                '}';
    }
}

