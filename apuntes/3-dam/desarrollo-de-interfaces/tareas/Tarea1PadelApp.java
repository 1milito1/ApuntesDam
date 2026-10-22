/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tarea1padelapp;

/**
 *
 * @author milio
 */
public class Tarea1PadelApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
     try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | javax.swing.UnsupportedLookAndFeelException ex) {
            System.err.println("Error al configurar Look and Feel: " + ex.getMessage());
        }
        
  
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                // Crear una instancia de la ventana principal
                VentanaPrincipal ventana = new VentanaPrincipal();
                
                // Centrar la ventana en la pantalla (mejor experiencia de usuario)
                ventana.setLocationRelativeTo(null);
                
                // Hacer visible la ventana de bienvenida
                ventana.setVisible(true);
            }
        });
    }
    
}
