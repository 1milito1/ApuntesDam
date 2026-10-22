package com.example.examen;

public class Entrada {

    private int id;
    private String partido;
    private float precio;
    private int cantidad;
    private String sitio;

    public Entrada(){

    }

    public Entrada(int id,String partido, float precio, int cantidad, String sitio) {
        this.id=id;
        this.partido = partido;
        this.precio = precio;
        this.cantidad = cantidad;
        this.sitio = sitio;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getPartido() {
        return this.partido;
    }

    public void setPartido(String partido) {
        this.partido = partido;
    }

    public float getPrecio() {
        return this.precio;
    }

    public void setPrecio(float precio) {
        this.precio = precio;
    }

    public int getCantidad() {
        return this.cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    public String getSitio() {
        return this.sitio;
    }

    public void setSitio(String sitio) {
        this.sitio = sitio;
    }

    public String toString(){
        return ("Id:"+this.id+"\n"+"Partido:"+this.partido+"\n"+"Cantidad:"+this.cantidad+"\n"+"Sitio:"+this.sitio);
    }

}




