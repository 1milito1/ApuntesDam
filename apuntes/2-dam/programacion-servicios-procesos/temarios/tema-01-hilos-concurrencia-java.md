# Tema 1: Procesos, Hilos y Concurrencia en Java
**Asignatura**: Programación de Servicios y Procesos (PSP) - 2º DAM  

## 1. Proceso vs Hilo
- **Proceso**: Programa en ejecución con su propio espacio de memoria aislado e independiente.
- **Hilo (Thread)**: Unidad básica de ejecución dentro de un proceso. Comparte memoria (heap) con otros hilos del mismo proceso.

---

## 2. Creación de Hilos en Java
### Mediante `Runnable` (Recomendado):
```java
Runnable tarea = () -> {
    System.out.println("Ejecutando en hilo: " + Thread.currentThread().getName());
};

Thread hilo = new Thread(tarea, "MiHiloWorker");
hilo.start(); // ¡Importante: start(), NO run()!
```

---

## 3. Secciones Críticas y `synchronized`
Cuando varios hilos acceden y modifican una misma variable compartida sin sincronizar, se produce una **condición de carrera** (*race condition*).

```java
public class ContadorSincronizado {
    private int valor = 0;

    public synchronized void incrementar() {
        valor++;
    }

    public synchronized int getValor() {
        return valor;
    }
}
```