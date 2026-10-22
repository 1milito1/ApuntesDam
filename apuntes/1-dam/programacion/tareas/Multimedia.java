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
public class Multimedia extends Movil {
    
    private int camara;
    private int fotos;
    
    public Multimedia(String numTelefono, String modelo, int fotos){
        super(numTelefono, modelo);
        this.camara = camara;
        this.fotos = 0 ;
    
}

    public int getCamara() {
        return camara;
    }

    public void setCamara(int camara) {
        this.camara = camara;
    }

    public int getFotos() {
        return fotos;
    }
    
    public void hacerFotos(){
        fotos++;
    }
    
    public void borraFotos(){
        if(fotos >0){
            fotos--;
        }
    }

    @Override
    public String toString() {
       return "Multimedia{" +
                "numTelefono='" + getNumTelefono() + '\'' +
                ", modelo='" + getModelo() + '\'' +
                ", llamadas=" + getLlamadas() +
                ", mensajes=" + getMensajes() +
                ", camara=" + camara +
                ", fotos=" + fotos +
                '}';
    }
    
}
