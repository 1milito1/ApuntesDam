# Tema 3: Diseño Relacional y Consultas SQL
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