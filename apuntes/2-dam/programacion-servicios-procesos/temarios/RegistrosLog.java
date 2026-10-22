/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gestioncafeteria;

/**
 *
 * @author milio
 */
class RegistrosLog {
    
    private final StringBuilder log = new StringBuilder();
    
    public synchronized void log (String mensaje) {
        log.append(mensaje).append("\n");
        System.out.println(mensaje);
    }
    
    public synchronized String getLog(){
        return log.toString();
    }
    
    
}
