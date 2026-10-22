/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea08telefonografico;

import java.io.*;

public class GestorArchivo {
    public static void guardarEstructura(ListaTelefono listaTelefono, String nombreArchivo) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nombreArchivo))) {
            oos.writeObject(listaTelefono);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static ListaTelefono cargarEstructura(String nombreArchivo) {
        ListaTelefono listaTelefono = null;
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nombreArchivo))) {
            listaTelefono = (ListaTelefono) ois.readObject();
        } catch (FileNotFoundException e) {
            // Si el archivo no existe, devolvemos una nueva instancia de ListaTelefono
            listaTelefono = new ListaTelefono();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return listaTelefono;
    }
}
