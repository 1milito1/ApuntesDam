/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gestioncafeteria;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.Semaphore;

/**
 *
 * @author milio
 */
public class GestionCafeteria {

    /**
     * @param args the command line arguments
     */
    
    private static final int NumeroMaquinas = 3;
    private static final Semaphore[] maquinas = new Semaphore[NumeroMaquinas];
    private static final BlockingQueue<Cliente> colaClientes = new LinkedBlockingQueue<>();
    private static final RegistrosLog registrosLog = new RegistrosLog();
    private static final int [] pedidosPorMaquina = new int [NumeroMaquinas];
    private static final int[][] tiposBebidasPorMaquina = new int [NumeroMaquinas][3];
    
    
    
    
    public static void main(String[] args) {
        // TODO code application logic here
        
        for (int i = 0; i < NumeroMaquinas; i++) {
            maquinas[i] = new Semaphore(1);
            
        }
        Thread gestorCola = new Thread (() -> {
            while (true) {
                try {
                    Cliente cliente = colaClientes.take();
                    boolean asignado = false;
                    
                    while (!asignado){
                        for (int i = 0; i < NumeroMaquinas; i++) {
                            if (maquinas[i].tryAcquire()) {
                                pedidosPorMaquina[i]++;
                                int tipoBebida;
                                switch (cliente.bebida) {
                                    case "Cafe":
                                        tipoBebida = 0;                                        
                                        break;
                                    case "Te":
                                        tipoBebida = 1;
                                        break;
                                    case "Chocolate Caliente":
                                        tipoBebida = 2;
                                        break;
                                    default:
                                        tipoBebida = -1;
                                        registrosLog.log("Bebida no encontada para cliente" + cliente.id);
                                        break;
                                }
                                if (tipoBebida != -1) {
                                    tiposBebidasPorMaquina[i][tipoBebida]++;
                                                                        
                                }
                                new Thread (new Cliente(cliente.id, cliente.bebida, maquinas[i], i + 1, registrosLog)).start();
                                asignado = true;
                                break;
                                
                            }
                            
                        }
                        if (!asignado) {
                            Thread.sleep(100);
                            
                        }
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
                
            }
        });
        
        
        gestorCola.start();
        
        String[] bebidas = {"Cafe", "Te", "Chocolate Caliente"};
        for (int i = 0; i < 10; i++) {
            String bebida = bebidas [(int) (Math.random() * bebidas.length)];
            try {
                colaClientes.put(new Cliente (i, bebida, null, -1, registrosLog));
                registrosLog.log("Cliente" + i + "ha llegado a la cola para pedir: " + bebida);
                
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            try {
                Thread.sleep(500);
                
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
            try {
                Thread.sleep(3500);
                
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            registrosLog.log("Resumen de pedidos por maquinas:");
            int totalPedidos = 0;
            for (int i = 0; i < NumeroMaquinas; i++) {
                int cafe = tiposBebidasPorMaquina [i] [0];
                int te = tiposBebidasPorMaquina [i][1];
                int chocolate = tiposBebidasPorMaquina[i][2];
                int totalMaquina = cafe + te + chocolate;
                totalPedidos += totalMaquina;
                registrosLog.log("Maquina " + (i+1) + ": " + totalMaquina + "pedidos: (Café= " + cafe + ", " + "Té= " + te + ", " + "Chocolate caliente= " + chocolate + ".)");
                
            }
            registrosLog.log("Total de pedidos atendidos= " + totalPedidos);
            
        
    }
    
}
