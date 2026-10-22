# Tema 2: Persistencia con Hibernate y JPA
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