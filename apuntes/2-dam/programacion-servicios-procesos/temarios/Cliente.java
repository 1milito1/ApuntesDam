/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gestioncafeteria;

import java.util.concurrent.Semaphore;

/**
 *
 * @author milio
 */
class Cliente implements Runnable {
    
    final int id;
    final String bebida;
    private final Semaphore semaforo;
    private final int maquinaId;
    private final RegistrosLog registrosLog;

    public Cliente(int id, String bebida, Semaphore semaforo, int maquinaId, RegistrosLog registrosLog) {
        this.id = id;
        this.bebida = bebida;
        this.semaforo = semaforo;
        this.maquinaId = maquinaId;
        this.registrosLog = registrosLog;
    }

     

    @Override
    public void run() {
    
        try {
            registrosLog.log("Cliente" + id + " está siendo atendido en la máquina: " + maquinaId + "para preparar " + bebida);
            int tiempoPreparacion = 0;
            switch (bebida) {
                case "Cafe":
                    tiempoPreparacion = 2000;
                    break;
                case "Te":
                    tiempoPreparacion = 1500;
                    break;
                case "Chocolate Caliente":
                    tiempoPreparacion = 2500;
                    break;               
                
                default:
                    registrosLog.log ("bebida no reconocida para cliente" + id);
                    return;
            }
            Thread.sleep(tiempoPreparacion);
            registrosLog.log ("Cliente" + id + "ha terminado de preaprar su " + bebida + "en la maquina " + maquinaId);
            
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            
        } finally {
            semaforo.release();
        }
    
    
    }
    
    
}
