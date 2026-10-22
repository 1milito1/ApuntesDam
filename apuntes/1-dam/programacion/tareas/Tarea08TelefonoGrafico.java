/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea08telefonografico;


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Tarea08TelefonoGrafico extends JFrame {

    private JTextField tfNumero, tfModelo, tfNumeroLlamada, tfNumeroMensaje;
    private JTextArea taMostrarTelefonos, taMensajes;
    private JRadioButton rbFijo, rbMovil, rbSmartphone;
    private JButton btnNuevo, btnLlamar, btnEnviarSMS, btnHacerFoto, btnBorrarFoto, btnMostrar, btnGuardarSalir;
    private ButtonGroup bgTipo;
    private ListaTelefono listaTelefonos;

    public Tarea08TelefonoGrafico() {
        initComponents();
        listaTelefonos = new ListaTelefono();
    }

    private void initComponents() {
        setTitle("Gestión de Teléfonos");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        add(panel);

        // Crear teléfono
        JPanel panelCrear = new JPanel(new FlowLayout());
        panelCrear.setBorder(BorderFactory.createTitledBorder("Crear teléfono"));

        tfNumero = new JTextField(10);
        tfModelo = new JTextField(10);
        btnNuevo = new JButton("Nuevo");

        rbFijo = new JRadioButton("fijo");
        rbMovil = new JRadioButton("móvil");
        rbSmartphone = new JRadioButton("smartPhone");

        bgTipo = new ButtonGroup();
        bgTipo.add(rbFijo);
        bgTipo.add(rbMovil);
        bgTipo.add(rbSmartphone);

        panelCrear.add(new JLabel("Número"));
        panelCrear.add(tfNumero);
        panelCrear.add(new JLabel("Modelo"));
        panelCrear.add(tfModelo);
        panelCrear.add(btnNuevo);
        panelCrear.add(new JLabel("Tipo"));
        panelCrear.add(rbFijo);
        panelCrear.add(rbMovil);
        panelCrear.add(rbSmartphone);

        panel.add(panelCrear);

        // Usar teléfono
        JPanel panelUsar = new JPanel(new FlowLayout());
        panelUsar.setBorder(BorderFactory.createTitledBorder("Usar teléfono"));

        tfNumeroLlamada = new JTextField(10);
        tfNumeroMensaje = new JTextField(10);
        taMensajes = new JTextArea(5, 20);
        taMensajes.setLineWrap(true);
        taMensajes.setWrapStyleWord(true);

        btnLlamar = new JButton("Llamar a ...");
        btnEnviarSMS = new JButton("Enviar sms a ...");
        btnHacerFoto = new JButton("Hacer foto");
        btnBorrarFoto = new JButton("Borrar foto");

        panelUsar.add(new JLabel("Número"));
        panelUsar.add(tfNumeroLlamada);
        panelUsar.add(btnLlamar);
        panelUsar.add(new JLabel("Número"));
        panelUsar.add(tfNumeroMensaje);
        panelUsar.add(btnEnviarSMS);
        panelUsar.add(new JScrollPane(taMensajes));
        panelUsar.add(btnHacerFoto);
        panelUsar.add(btnBorrarFoto);

        panel.add(panelUsar);

        // Mostrar teléfonos
        JPanel panelMostrar = new JPanel(new FlowLayout());
        panelMostrar.setBorder(BorderFactory.createTitledBorder("Mostrar teléfonos"));

        taMostrarTelefonos = new JTextArea(5, 40);
        taMostrarTelefonos.setLineWrap(true);
        taMostrarTelefonos.setWrapStyleWord(true);
        taMostrarTelefonos.setEditable(false);

        btnMostrar = new JButton("Mostrar");

        panelMostrar.add(new JScrollPane(taMostrarTelefonos));
        panelMostrar.add(btnMostrar);

        panel.add(panelMostrar);

        // Guardar y salir
        btnGuardarSalir = new JButton("Guardar y Salir");

        panel.add(btnGuardarSalir);

        // Action Listeners
        btnNuevo.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                crearTelefono();
            }
        });

        btnLlamar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                llamarTelefono();
            }
        });

        btnEnviarSMS.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                enviarSMS();
            }
        });

        btnHacerFoto.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                hacerFoto();
            }
        });

        btnBorrarFoto.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                borrarFoto();
            }
        });

        btnMostrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mostrarTelefonos();
            }
        });

        btnGuardarSalir.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                guardarYSalir();
            }
        });
    }

    private void crearTelefono() {
        String numero = tfNumero.getText();
        String modelo = tfModelo.getText();
        Telefono telefono;

        if (rbFijo.isSelected()) {
            telefono = new Telefono(numero, modelo);
        } else if (rbMovil.isSelected()) {
            telefono = new Movil(numero, modelo);
        } else if (rbSmartphone.isSelected()) {
            telefono = new Multimedia(numero, modelo, 0);
        } else {
            JOptionPane.showMessageDialog(this, "Seleccione un tipo de teléfono");
            return;
        }

        listaTelefonos.agreagarTelefono(telefono);
        JOptionPane.showMessageDialog(this, "Teléfono creado");
        limpiarCamposCrear();
    }

    private void limpiarCamposCrear() {
        tfNumero.setText("");
        tfModelo.setText("");
        bgTipo.clearSelection();
    }

    private void llamarTelefono() {
        String numeroLlamada = tfNumeroLlamada.getText();
        String numeroTelefono = tfNumero.getText();

        Telefono telefono = listaTelefonos.buscarTelefono(numeroTelefono);
        if (telefono != null) {
            telefono.llamarA(numeroLlamada);
            JOptionPane.showMessageDialog(this, "Llamada realizada a " + numeroLlamada);
        } else {
            JOptionPane.showMessageDialog(this, "Teléfono no encontrado");
        }
        tfNumeroLlamada.setText("");
    }

    private void enviarSMS() {
        String numeroMensaje = tfNumeroMensaje.getText();
        String mensajeTexto = taMensajes.getText();
        String numeroTelefono = tfNumero.getText();

        Telefono telefono = listaTelefonos.buscarTelefono(numeroTelefono);
        if (telefono != null && telefono instanceof Movil) {
            Movil movil = (Movil) telefono;
            Mensaje mensaje = new Mensaje(numeroMensaje, mensajeTexto);
            movil.enviarSMS(mensaje);
            JOptionPane.showMessageDialog(this, "Mensaje enviado a " + numeroMensaje);
        } else {
            JOptionPane.showMessageDialog(this, "Teléfono móvil no encontrado o no es un móvil");
        }
        tfNumeroMensaje.setText("");
        taMensajes.setText("");
    }

    private void hacerFoto() {
        String numeroTelefono = tfNumero.getText();

        Telefono telefono = listaTelefonos.buscarTelefono(numeroTelefono);
        if (telefono != null && telefono instanceof Multimedia) {
            Multimedia multimedia = (Multimedia) telefono;
            multimedia.hacerFotos();
            JOptionPane.showMessageDialog(this, "Foto hecha");
        } else {
            JOptionPane.showMessageDialog(this, "Teléfono multimedia no encontrado o no es multimedia");
        }
    }

    private void borrarFoto() {
        String numeroTelefono = tfNumero.getText();

        Telefono telefono = listaTelefonos.buscarTelefono(numeroTelefono);
        if (telefono != null && telefono instanceof Multimedia) {
            Multimedia multimedia = (Multimedia) telefono;
            multimedia.borraFotos();
            JOptionPane.showMessageDialog(this, "Foto borrada");
        } else {
            JOptionPane.showMessageDialog(this, "Teléfono multimedia no encontrado o no es multimedia");
        }
    }

    private void mostrarTelefonos() {
        taMostrarTelefonos.setText("");
        for (Telefono telefono : listaTelefonos.getTelefonos()) {
            taMostrarTelefonos.append(telefono.toString() + "\n");
        }
    }

    private void guardarYSalir() {
        GestorArchivo.guardarEstructura(listaTelefonos, "telefonos.dat");
        System.exit(0);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new Tarea08TelefonoGrafico().setVisible(true);
            }
        });
    }
}