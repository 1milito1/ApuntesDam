-- ========================================================
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