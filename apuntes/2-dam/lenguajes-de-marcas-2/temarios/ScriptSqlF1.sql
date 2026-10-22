-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS BDTarea;
USE BDTarea;

-- Crear la tabla
CREATE TABLE IF NOT EXISTS Carreras (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre_circuito VARCHAR(255) NOT NULL,
fecha DATE NOT NULL,
num_vueltas INT,
piloto_ganador VARCHAR(255),
detalles_carrera JSON);
 
 -- Insertar 3 Registros en la tabla 
INSERT INTO Carreras (nombre_circuito, fecha, num_vueltas, piloto_ganador, detalles_carrera)
VALUES (
	'Circuito de mónaco',
	'2025-05-25',
	78,
	'Max Verstappen',
	'{ "condiciones_climaticas": ["seco", "soleado"],
	"incidentes" : {
		"vuelta_5": "Safety Car por accidente",
		"vuelta_30": "Bandera amarilla sector 2" 
	}
}'
);

INSERT INTO Carreras (nombre_circuito, fecha, num_vueltas, piloto_ganador, detalles_carrera)
VALUES (
	'Silverstone',
	'2025-07-06',
	52,
	'Lewis Hamilton',
	'{ "neumaticos_utilizados": ["medio", "duro", "medio"],
	"estrategia_paradas": {
		"piloto_1": 2,
		"piloto_2": 3
	}
}'
);


INSERT INTO Carreras (nombre_circuito, fecha, num_vueltas, piloto_ganador, detalles_carrera)
VALUES (
	'Monza',
	'2025-09-07',
	52,
	'Carlos Sainz',
	'{ "velocidad_punta": [345.6, 348.1, 342.9],
	"fallos__mecanicios":{
		"piloto_x": "Problema en la unidad de pontecia"
		}
	}'
);

-- Sentencia con filtro y ordenación por campo JSON
SELECT nombre_circuito, detalles_carrera -> '$.condiciones_climaticas' AS condiciones
FROM Carreras
WHERE detalles_carrera->'$.incidentes.vuelta_5' = 'Safety Car por accidente'
ORDER BY detalles_carrera->'$.condiciones_climaticas[0]';

-- Modficar un valor de una clave JSON
UPDATE Carreras
SET detalles_carrera = JSON_SET(detalles_carrera, '$.incidentes.vuelta_5', 'Accidente grave con bandera roja')
WHERE nombre_circuito = 'Circuito de Mónaco';

-- Añadir una nueva Clave-Valor al JSON
UPDATE Carreras
SET detalles_carrera = JSON_SET(detalles_carrera, '$.espectadores', 350000)
WHERE nombre_circuito = 'Silverstone';

-- Eliminar una clave de un objeto
UPDATE Carreras
SET detalles_carrera = JSON_REMOVE(detalles_carrera, '$.fallos_mecanicos')
WHERE nombre_circuito = 'Monza';

-- Añadir un array
UPDATE Carreras
SET detalles_carrera = JSON_ARRAY_APPEND(detalles_carrera, '$.condiciones_climaticas', 'lluvia ligera')
WHERE nombre_circuito = 'Circuito de Mónaco';

-- Modificar un array
UPDATE Carreras
SET detalles_carrera = JSON_REPLACE(detalles_carrera, '$.meumaticos_utilizados[0]', 'blando')
WHERE nombre_circuito = 'Silverstone';