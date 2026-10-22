# Tema 4: Programación Orientada a Objetos en Java
**Ciclo Formativo**: DAM 1º - Programación  
**Autor**: Apuntes DAM  
**Última actualización**: 2026-10-15  

---

## 1. Conceptos Fundamentales
La Programación Orientada a Objetos (POO) es un paradigma de programación basado en el concepto de "objetos", los cuales contienen datos en forma de campos (atributos) y código en forma de procedimientos (métodos).

### Los 4 Pilares de la POO:
1. **Encapsulamiento**: Ocultar el estado interno y obligar a interactuar mediante métodos públicos (getters/setters).
2. **Abstracción**: Modelar las características esenciales de un objeto ignorando detalles secundarios.
3. **Herencia**: Capacidad de una clase hija de heredar atributos y métodos de una clase padre (`extends`).
4. **Polimorfismo**: Capacidad de responder de diferentes maneras al mismo mensaje según el tipo de objeto en tiempo de ejecución.

---

## 2. Ejemplo Práctico: Jerarquía de Vehículos

```java
// Clase abstracta base
public abstract class Vehiculo {
    private String matricula;
    private String marca;
    private double velocidadActual;

    public Vehiculo(String matricula, String marca) {
        this.matricula = matricula;
        this.marca = marca;
        this.velocidadActual = 0.0;
    }

    public abstract void acelerar(double incremento);

    public String getMatricula() {
        return matricula;
    }

    public double getVelocidadActual() {
        return velocidadActual;
    }

    protected void setVelocidadActual(double v) {
        this.velocidadActual = v;
    }
}
```

```java
// Subclase que hereda de Vehiculo
public class Coche extends Vehiculo {
    private int numPuertas;

    public Coche(String matricula, String marca, int numPuertas) {
        super(matricula, marca);
        this.numPuertas = numPuertas;
    }

    @Override
    public void acelerar(double incremento) {
        double nuevaVel = getVelocidadActual() + (incremento * 1.2);
        setVelocidadActual(nuevaVel);
        System.out.println("Coche acelerando a " + nuevaVel + " km/h");
    }
}
```

---

## 3. Interfaces vs Clases Abstractas
| Característica | Clase Abstracta | Interfaz (`interface`) |
| :--- | :--- | :--- |
| **Herencia múltiple** | No (solo 1 clase padre con `extends`) | Sí (múltiples con `implements`) |
| **Constructores** | Sí puede tener | No |
| **Variables de instancia** | Sí puede tener cualquier visibilidad | Solo constantes (`public static final`) |
| **Métodos por defecto** | Métodos con código y abstractos | Métodos abstractos o `default` (Java 8+) |

---

## 4. Consejos para el examen
- Recordar siempre usar `@Override` al sobreescribir métodos.
- En constructores de subclases, la llamada a `super(...)` debe ser la **primera línea**.
- Las colecciones polimórficas se declaran con la interfaz: `List<Vehiculo> lista = new ArrayList<>();`.