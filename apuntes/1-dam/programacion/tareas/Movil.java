/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea08telefonografico;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

/**
 *
 * @author milio
 */
public class Movil extends Telefono {
    
    private List <Mensaje> mensajes;

    public Movil(String Telefono, String Modelo) {
        super(Telefono, Modelo);
        this.mensajes = new ArrayList<>();
        
    }
    
    public List<Mensaje> getMensajes(){
        return mensajes;
    }
    
    public void enviarSMS(Mensaje nuevoMensaje){
        mensajes.add(nuevoMensaje);
    }

    @Override
    public String toString() {
        return "Movil{" +
                "numTelefono='" + getNumTelefono() + '\'' +
                ", modelo='" + getModelo() + '\'' +
                ", llamadas=" + getLlamadas() +
                ", mensajes=" + mensajes +
                '}';
    }
    
    
}
