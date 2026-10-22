# Chuleta de Colecciones y Streams en Java
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