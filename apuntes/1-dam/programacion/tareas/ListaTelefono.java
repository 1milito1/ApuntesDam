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
public class ListaTelefono {
    private Set<Telefono> telefonos;
    
    public ListaTelefono(){
        telefonos = new HashSet<>(); 
        
    }
    
    public void agreagarTelefono (Telefono telefono){
        telefonos.add(telefono);
    }
    
    public Telefono buscarTelefono(String numTelefono){
        
        for (Telefono telefono : telefonos){
            if(telefono.getNumTelefono().equalsIgnoreCase(numTelefono)){
                return telefono;
            }
        }
        return null;
    }
    public void mostrarTelefonos(){
        for(Telefono telefono : telefonos){
            System.out.println(telefono);
        }
    }
    
    public Set<Telefono> getTelefonos(){
        return telefonos;
    }
    
}
