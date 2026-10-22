# Examen Oficial 1ª Evaluación - Programación DAM
**Duración**: 120 minutos  
**Calificación máxima**: 10 puntos  
**Puntuación**: Ej.1 (2.5p), Ej.2 (3p), Ej.3 (2.5p), Ej.4 (2p)  

---

## Ejercicio 1: Gestión de Empleados (2.5 puntos)
Crea una clase abstracta `Empleado` con nombre, dni y salarioBase. Luego implementa `EmpleadoComision` con porcentaje y ventas.

### Solución:
```java
public abstract class Empleado {
    private String dni;
    private String nombre;
    private double salarioBase;

    public Empleado(String dni, String nombre, double salarioBase) {
        this.dni = dni;
        this.nombre = nombre;
        this.salarioBase = salarioBase;
    }

    public abstract double calcularSalarioTotal();

    public double getSalarioBase() { return salarioBase; }
}

public class EmpleadoComision extends Empleado {
    private double ventasMes;
    private double porcentajeComision; // ej: 0.05 para 5%

    public EmpleadoComision(String dni, String nombre, double salarioBase, double ventasMes, double comision) {
        super(dni, nombre, salarioBase);
        this.ventasMes = ventasMes;
        this.porcentajeComision = comision;
    }

    @Override
    public double calcularSalarioTotal() {
        return getSalarioBase() + (ventasMes * porcentajeComision);
    }
}
```

---

## Errores habituales en el examen
1. Olvidar validar si las ventas son negativas.
2. Usar tipos `int` para dinero en lugar de `double` o `BigDecimal`.
3. No declarar el método como `abstract` en la clase padre.