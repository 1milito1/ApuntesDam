import os
import json
from datetime import datetime

BASE_DIR = r"C:\Users\milio\.gemini\antigravity-ide\scratch\dam-apuntes"

SAMPLE_FILES = [
    {
        "rel_path": "apuntes/1-dam/programacion/temarios/tema-04-poo-clases-objetos.md",
        "title": "Tema 4: Programación Orientada a Objetos en Java",
        "curso": "1-dam",
        "asignatura": "programacion",
        "categoria": "temarios",
        "tags": ["Java", "POO", "Clases", "Herencia", "Polimorfismo"],
        "description": "Explicación detallada de clases, constructores, encapsulamiento, herencia, interfaces y polimorfismo con ejemplos claros en Java.",
        "content": """# Tema 4: Programación Orientada a Objetos en Java
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
"""
    },
    {
        "rel_path": "apuntes/1-dam/programacion/examenes/examen-1eval-poo-resuelto.md",
        "title": "Examen 1ª Evaluación: Java y POO (Resuelto y Comentado)",
        "curso": "1-dam",
        "asignatura": "programacion",
        "categoria": "examenes",
        "tags": ["Examen", "Java", "Solución", "POO", "1ª Evaluación"],
        "description": "Examen oficial de la primera evaluación con 5 ejercicios prácticos resueltos paso a paso y criterios de corrección.",
        "content": """# Examen Oficial 1ª Evaluación - Programación DAM
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
"""
    },
    {
        "rel_path": "apuntes/1-dam/programacion/recursos/chuleta-java-colecciones-streams.md",
        "title": "Chuleta Rápida: Colecciones, Mapas y Streams en Java",
        "curso": "1-dam",
        "asignatura": "programacion",
        "categoria": "recursos",
        "tags": ["Chuleta", "Java", "Collections", "List", "Map", "Streams"],
        "description": "Resumen imprescindible de sintaxis para ArrayList, HashMap, HashSet y operaciones habituales con Java Stream API.",
        "content": """# Chuleta de Colecciones y Streams en Java
*Guía rápida para consultas en clase y exámenes prácticos.*

## 1. Listas (`ArrayList`)
```java
List<String> alumnos = new ArrayList<>();
alumnos.add("Lucía");
alumnos.add(0, "Marcos"); // Inserta en posición 0
alumnos.remove("Marcos");
alumnos.contains("Lucía"); // true
alumnos.size();
```

## 2. Conjuntos (`HashSet` / `TreeSet`)
```java
// No admite duplicados
Set<Integer> codigos = new HashSet<>();
codigos.add(101);
codigos.add(101); // Se ignora silenciosamente

// TreeSet ordena los elementos de forma natural
Set<String> ordenados = new TreeSet<>();
```

## 3. Mapas Clave-Valor (`HashMap`)
```java
Map<String, Double> notas = new HashMap<>();
notas.put("12345678A", 8.75);
notas.put("87654321B", 6.50);

// Recorrer mapa eficientemente
for (Map.Entry<String, Double> entry : notas.entrySet()) {
    System.out.println("DNI: " + entry.getKey() + " -> Nota: " + entry.getValue());
}
```

## 4. Streams en 1 minuto
```java
// Filtrar, transformar y recolectar
List<String> aprobados = alumnos.stream()
    .filter(a -> notas.getOrDefault(a.getDni(), 0.0) >= 5.0)
    .map(Alumno::getNombre)
    .sorted()
    .collect(Collectors.toList());
```
"""
    },
    {
        "rel_path": "apuntes/1-dam/bases-de-datos/temarios/tema-03-modelo-relacional-sql.md",
        "title": "Tema 3: Diseño Relacional y Consultas SQL (DML / DDL)",
        "curso": "1-dam",
        "asignatura": "bases-de-datos",
        "categoria": "temarios",
        "tags": ["Bases de Datos", "SQL", "MySQL", "PostgreSQL", "DDL", "DML"],
        "description": "Fundamentos del modelo relacional, claves primarias/foráneas, cláusulas SELECT, JOINs y funciones de agregación.",
        "content": """# Tema 3: Diseño Relacional y Consultas SQL
**Asignatura**: Bases de Datos (1º DAM)

## 1. Claves y Restricciones
- **Primary Key (PK)**: Identificador único de cada fila. No puede ser NULL ni repetirse.
- **Foreign Key (FK)**: Referencia a una PK en otra tabla para asegurar integridad referencial.
- **UNIQUE**: Evita duplicados pero admite valores nulos.
- **CHECK**: Valida condiciones (ej. `CHECK (edad >= 18)`).

---

## 2. Los tipos de JOIN ilustrados
```sql
-- INNER JOIN: Filas con coincidencia en ambas tablas
SELECT c.nombre, p.numero_pedido, p.importe
FROM clientes c
INNER JOIN pedidos p ON c.id_cliente = p.id_cliente;

-- LEFT JOIN: Todos los clientes, tengan pedidos o no
SELECT c.nombre, COUNT(p.id_pedido) as total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente, c.nombre;
```

---

## 3. Cláusula HAVING vs WHERE
- `WHERE`: Filtra filas **antes** de agrupar.
- `HAVING`: Filtra grupos **después** de aplicar `GROUP BY`.

```sql
SELECT departamento_id, AVG(salario) as salario_medio
FROM empleados
WHERE activo = 1
GROUP BY departamento_id
HAVING AVG(salario) > 2500;
```
"""
    },
    {
        "rel_path": "apuntes/1-dam/bases-de-datos/recursos/chuleta-comandos-sql-ddl-dml.sql",
        "title": "Script / Chuleta: Comandos SQL DDL y DML Frecuentes",
        "curso": "1-dam",
        "asignatura": "bases-de-datos",
        "categoria": "recursos",
        "tags": ["SQL", "Chuleta", "DDL", "DML", "CheatSheet"],
        "description": "Colección de sentencias SQL listas para copiar: CREATE TABLE, ALTER TABLE, subconsultas y transacciones.",
        "content": """-- ========================================================
-- CHULETA RÁPIDA SQL: DDL, DML Y TRANSACCIONES
-- Ciclo DAM - Bases de Datos
-- ========================================================

-- 1. CREACIÓN DE TABLAS CON RESTRICCIONES
CREATE TABLE IF NOT EXISTS modulos_dam (
    id_modulo INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    horas_semana INT DEFAULT 4 CHECK (horas_semana > 0),
    curso ENUM('1', '2') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. MODIFICACIÓN DE TABLAS (ALTER)
ALTER TABLE modulos_dam ADD COLUMN docente VARCHAR(80) AFTER nombre;
ALTER TABLE modulos_dam DROP COLUMN horas_semana;

-- 3. INSERTAR DATOS
INSERT INTO modulos_dam (codigo, nombre, docente, curso) VALUES
('PROG', 'Programación', 'Prof. García', '1'),
('BBDD', 'Bases de Datos', 'Prof. Martínez', '1'),
('AD', 'Acceso a Datos', 'Prof. Sánchez', '2');

-- 4. CONSULTA AVANZADA CON SUBCONSULTAS
SELECT nombre, curso
FROM modulos_dam
WHERE id_modulo IN (
    SELECT id_modulo FROM matriculas WHERE calificacion >= 5.0
);
"""
    },
    {
        "rel_path": "apuntes/1-dam/entornos-de-desarrollo/recursos/chuleta-comandos-git.md",
        "title": "Guía Rápida de Git y Flujo de Trabajo en GitHub",
        "curso": "1-dam",
        "asignatura": "entornos-de-desarrollo",
        "categoria": "recursos",
        "tags": ["Git", "GitHub", "Control de Versiones", "Ramas", "Terminal"],
        "description": "Guía completa de comandos de Git: init, clone, add, commit, push, pull, ramas, merge y resolución de conflictos.",
        "content": """# Guía Rápida de Git para DAM
*Aprende a dominar el control de versiones en tus proyectos.*

## 1. Configuración Inicial
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@gmail.com"
```

## 2. Flujo Diario de Trabajo
```bash
git status               # Ver archivos modificados
git add .                # Añadir todos los cambios al stage
git commit -m "Mensaje"  # Confirmar cambios
git push origin main     # Subir al repositorio remoto
```

## 3. Trabajo con Ramas (Branches)
```bash
git checkout -b feature/login    # Crear y cambiar a nueva rama
git branch                       # Listar ramas locales
git checkout main                # Volver a main
git merge feature/login          # Fusionar rama en la actual
```
"""
    },
    {
        "rel_path": "apuntes/2-dam/acceso-a-datos/temarios/tema-02-mapeo-orm-hibernate-jpa.md",
        "title": "Tema 2: Persistencia y ORM con Hibernate y JPA",
        "curso": "2-dam",
        "asignatura": "acceso-a-datos",
        "categoria": "temarios",
        "tags": ["Hibernate", "JPA", "Acceso a Datos", "Java", "ORM", "Entity"],
        "description": "Mapeo objeto-relacional en Java: anotaciones @Entity, @Id, @OneToMany, EntityManager y consultas JPQL.",
        "content": """# Tema 2: Persistencia con Hibernate y JPA
**Ciclo Formativo**: DAM 2º - Acceso a Datos  

## 1. ¿Qué es un ORM?
Un Object-Relational Mapper (ORM) traduce las filas de una base de datos relacional a objetos de un lenguaje orientado a objetos, reduciendo el código repetitivo de JDBC.

## 2. Anotaciones Esenciales de JPA
```java
import jakarta.persistence.*;
import java.util.List;

@Entity
@Table(name = "proyectos")
public class Proyecto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "titulo", nullable = false, length = 150)
    private String titulo;

    @OneToMany(mappedBy = "proyecto", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Tarea> tareas;

    // Constructores, Getters y Setters
}
```

## 3. Consultas con JPQL
```java
// JPQL trabaja sobre las Clases y propiedades, no sobre tablas SQL
TypedQuery<Proyecto> query = em.createQuery(
    "SELECT p FROM Proyecto p WHERE p.titulo LIKE :parametro", Proyecto.class
);
query.setParameter("parametro", "%DAM%");
List<Proyecto> resultados = query.getResultList();
```
"""
    },
    {
        "rel_path": "apuntes/2-dam/acceso-a-datos/examenes/simulacro-examen-jdbc-hibernate.md",
        "title": "Simulacro de Examen: JDBC, DAO Pattern e Hibernate",
        "curso": "2-dam",
        "asignatura": "acceso-a-datos",
        "categoria": "examenes",
        "tags": ["Examen", "Acceso a Datos", "JDBC", "DAO", "Hibernate"],
        "description": "Simulacro de examen práctico con enunciado, diagrama relacional y solución con patrón DAO y PreparedStatement.",
        "content": """# Simulacro Examen Acceso a Datos (2º DAM)
**Tema**: Patrón DAO, JDBC con Transacciones y Configuración Hibernate.  

## Enunciado
Implementa un método `transferirFondos(Long origen, Long destino, Double cantidad)` que ejecute la transacción de forma atómica usando JDBC nativo, gestionando `setAutoCommit(false)`, `commit()` y `rollback()` en caso de excepción.

```java
public void transferirFondos(Long origen, Long destino, Double cantidad) throws SQLException {
    Connection conn = null;
    try {
        conn = DatabaseConnection.getConnection();
        conn.setAutoCommit(false); // Iniciar transacción

        // 1. Restar de cuenta origen
        try (PreparedStatement psRetirar = conn.prepareStatement(
                "UPDATE cuentas SET saldo = saldo - ? WHERE id = ? AND saldo >= ?")) {
            psRetirar.setDouble(1, cantidad);
            psRetirar.setLong(2, origen);
            psRetirar.setDouble(3, cantidad);
            int filas = psRetirar.executeUpdate();
            if (filas == 0) {
                throw new SQLException("Saldo insuficiente o cuenta origen inexistente.");
            }
        }

        // 2. Ingresar en cuenta destino
        try (PreparedStatement psIngresar = conn.prepareStatement(
                "UPDATE cuentas SET saldo = saldo + ? WHERE id = ?")) {
            psIngresar.setDouble(1, cantidad);
            psIngresar.setLong(2, destino);
            psIngresar.executeUpdate();
        }

        conn.commit(); // Confirmar todo
        System.out.println("Transferencia realizada con éxito.");

    } catch (SQLException e) {
        if (conn != null) conn.rollback(); // Deshacer cambios
        throw e;
    } finally {
        if (conn != null) conn.setAutoCommit(true);
    }
}
```
"""
    },
    {
        "rel_path": "apuntes/2-dam/programacion-servicios-procesos/temarios/tema-01-hilos-concurrencia-java.md",
        "title": "Tema 1: Procesos, Hilos (Threads) y Concurrencia",
        "curso": "2-dam",
        "asignatura": "programacion-servicios-procesos",
        "categoria": "temarios",
        "tags": ["PSP", "Hilos", "Threads", "Concurrencia", "Synchronized"],
        "description": "Ciclo de vida de un hilo, interfaz Runnable, Thread pool con ExecutorService y sincronización de recursos compartidos.",
        "content": """# Tema 1: Procesos, Hilos y Concurrencia en Java
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
"""
    },
    {
        "rel_path": "apuntes/2-dam/programacion-multimedia/recursos/guia-ciclo-vida-activity-jetpack.md",
        "title": "Chuleta: Ciclo de Vida de Android Activity y Jetpack Compose",
        "curso": "2-dam",
        "asignatura": "programacion-multimedia",
        "categoria": "recursos",
        "tags": ["Android", "Kotlin", "PMDM", "Jetpack Compose", "Ciclo de Vida"],
        "description": "Diagrama y descripción de onCreate, onStart, onResume, onPause, onStop, onDestroy y estado en Compose.",
        "content": """# Ciclo de Vida de Android y Jetpack Compose
**Ciclo Formativo**: 2º DAM - Programación Multimedia y Dispositivos Móviles  

## Métodos del Ciclo de Vida (Activity):
1. **onCreate()**: Se llama al crear la actividad por primera vez. Inicializar componentes y vistas.
2. **onStart()**: La actividad se vuelve visible para el usuario.
3. **onResume()**: La actividad pasa al primer plano y tiene el foco de interacción.
4. **onPause()**: El usuario pierde foco parcial (ej. sale un diálogo flotante).
5. **onStop()**: La actividad ya no es visible para el usuario.
6. **onDestroy()**: La actividad va a ser destruida completamente de la memoria.

---

## Estado en Jetpack Compose
En Compose la UI se recompone automáticamente al cambiar el estado:
```kotlin
@Composable
fun ContadorInteractivo() {
    var contador by rememberSaveable { mutableStateOf(0) }

    Button(onClick = { contador++ }) {
        Text("Pulsaciones: $contador")
    }
}
```
"""
    }
]

# Write files and build json
docs_index = []

for idx, item in enumerate(SAMPLE_FILES, start=1):
    full_path = os.path.join(BASE_DIR, item["rel_path"].replace("/", os.sep))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(item["content"].strip())
    
    file_size_bytes = os.path.getsize(full_path)
    file_size_str = f"{file_size_bytes / 1024:.1f} KB" if file_size_bytes < 1024*1024 else f"{file_size_bytes / (1024*1024):.1f} MB"
    ext = os.path.splitext(item["rel_path"])[1].replace(".", "").lower()
    
    curso_map = {"1-dam": "1º DAM", "2-dam": "2º DAM"}
    asig_map = {
        "programacion": "Programación",
        "bases-de-datos": "Bases de Datos",
        "sistemas-informaticos": "Sistemas Informáticos",
        "entornos-de-desarrollo": "Entornos de Desarrollo",
        "lenguajes-de-marcas": "Lenguajes de Marcas",
        "fol-ipe": "FOL / IPE",
        "acceso-a-datos": "Acceso a Datos",
        "desarrollo-de-interfaces": "Desarrollo de Interfaces",
        "programacion-multimedia": "Prog. Multimedia y Móviles",
        "programacion-servicios-procesos": "Prog. Servicios y Procesos",
        "sistemas-gestion-empresarial": "Sistemas de Gestión Empresarial",
        "empresa-iniciativa": "Empresa e Iniciativa Emprendedora"
    }
    cat_map = {
        "temarios": "Temarios y Apuntes",
        "examenes": "Exámenes Anteriores",
        "tareas": "Tareas y Prácticas",
        "recursos": "Chuletas y Recursos de Ayuda"
    }

    doc = {
        "id": f"doc-{idx:03d}",
        "title": item["title"],
        "curso": item["curso"],
        "cursoName": curso_map.get(item["curso"], item["curso"]),
        "asignatura": item["asignatura"],
        "asignaturaName": asig_map.get(item["asignatura"], item["asignatura"]),
        "categoria": item["categoria"],
        "categoriaName": cat_map.get(item["categoria"], item["categoria"]),
        "relPath": item["rel_path"].replace("\\", "/"),
        "filename": os.path.basename(item["rel_path"]),
        "fileType": ext,
        "fileSize": file_size_str,
        "date": "2026-10-18",
        "tags": item["tags"],
        "description": item["description"]
    }
    docs_index.append(doc)

# Save JSON metadata
from init_data import STRUCTURE
data_to_save = {
    "version": "1.0.0",
    "lastUpdated": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "cursos": STRUCTURE["cursos"],
    "categorias": STRUCTURE["categorias"],
    "documentos": docs_index
}

json_path = os.path.join(BASE_DIR, "data", "apuntes.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data_to_save, f, ensure_ascii=False, indent=2)

# Also create a js/data.js that assigns window.APUNTES_DATA = ... so index.html works even under file:// protocol without CORS errors!
js_data_path = os.path.join(BASE_DIR, "js", "data.js")
with open(js_data_path, "w", encoding="utf-8") as f:
    f.write(f"// Datos precargados para compatibilidad total con file:// y GitHub Pages\nwindow.INITIAL_DATA = {json.dumps(data_to_save, ensure_ascii=False, indent=2)};\n")

print(f"Generated {len(docs_index)} sample documents and wrote data/apuntes.json + js/data.js")
