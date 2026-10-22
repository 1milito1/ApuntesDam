# Simulacro Examen Acceso a Datos (2º DAM)
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