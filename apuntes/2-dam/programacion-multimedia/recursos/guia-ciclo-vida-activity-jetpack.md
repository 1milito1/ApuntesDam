# Ciclo de Vida de Android y Jetpack Compose
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