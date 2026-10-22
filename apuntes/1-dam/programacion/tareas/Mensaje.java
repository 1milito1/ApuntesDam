/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea08telefonografico;

/**
 *
 * @author milio
 */
public class Mensaje {
    
    private String numTelefono;
    private String mensaje;

    public Mensaje(String numTelefono, String mensaje) {
        this.numTelefono = numTelefono;
        this.mensaje = mensaje;
    }

    public String getNumTelefono() {
        return numTelefono;
    }

    public void setNumTelefono(String numTelefono) {
        this.numTelefono = numTelefono;
    }

    public String getMensaje() {
        return mensaje;
    }

    public void setMensaje(String mensaje) {
        this.mensaje = mensaje;
    }

    @Override
    public String toString() {
        return "Mensaje{" + "numTelefono=" + numTelefono + ", mensaje=" + mensaje + '}';
    }
    
    
}
