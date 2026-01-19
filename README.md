# Hoja de Trabajo 1 - Agente Reflejo Simple

**Universidad del Valle de Guatemala**  
**Inteligencia Artificial - CC3045 - Sección 10**  
**Fecha:** 18/01/2026  
**Autores:**
- Daniel Chet - 231177
- Dulce Ambrosio - 231143

## Descripción del Proyecto

Este proyecto implementa un **Agente Reflejo Simple** (Simple Reflex Agent) para un entorno de "Termostato Inteligente" utilizando Programación Orientada a Objetos en Python puro. El agente es capaz de percibir la temperatura del ambiente y tomar decisiones para mantenerla en un rango confortable (18°C - 25°C).

## Objetivos

- Traducir la Arquitectura de Agente a una estructura de código orientado a objetos
- Implementar un ciclo de Percepción/Acción
- Demostrar el funcionamiento de un agente reactivo simple sin el uso de librerías de IA

## Arquitectura

El ejercicio está basado en la arquitectura clásica de agentes inteligentes, implementando los siguientes componentes:

### 1. **Ambiente (Environment)**
Representa el entorno con el que interactúa el agente.

**Componentes:**
- `temperatura`: Variable que almacena la temperatura actual (inicializada aleatoriamente entre 10°C y 30°C)
- `obtenertemperatura()`: Método sensor que retorna la percepción del ambiente
- `actualizartemperatura(accion)`: Método actuador que modifica el estado del ambiente según la acción recibida

### 2. **Agente (Agent)**
Implementa la lógica de decisión del agente reflejo simple.

**Componentes:**
- `accion(temperatura)`: Implementa la función f(estado) que mapea percepciones a acciones

**Reglas de decisión:**
```
Si temperatura > 25°C → "enfriar"
Si temperatura < 18°C → "calentar"
Si 18°C ≤ temperatura ≤ 25°C → "esperar"
```

### 3. **Main (Ciclo de Percepción/Acción)**
Implementa el loop principal que conecta el agente con el ambiente.

## Estructura del Proyecto

```
HojadeTrabajo1/
│
├── Ambiente.py      # Clase Environment
├── Agente.py        # Clase Agent
├── Main.py          # Programa principal
└── README.md        # Este archivo
```


## Salida Esperada

El programa ejecutará 10 iteraciones del ciclo percepción-acción, mostrando en cada paso:

```
Temperatura actual: 23 °C - Acción del agente: esperar - Nueva temperatura: 23 °C
Temperatura actual: 23 °C - Acción del agente: esperar - Nueva temperatura: 23 °C
Temperatura actual: 23 °C - Acción del agente: esperar - Nueva temperatura: 23 °C
...
```

Cada línea muestra:
- **Temperatura actual**: Estado percibido por el agente
- **Acción del agente**: Decisión tomada según las reglas
- **Nueva temperatura**: Estado resultante después de ejecutar la acción

## Detalles de Implementación

### Clase Ambiente

```python
class Ambiente:
    def __init__(self):
        # Temperatura inicial aleatoria entre 10 y 30 grados
        self.temperatura = randint(10, 30)
    
    def obtenertemperatura(self):
        # Simula sensores del ambiente
        return self.temperatura
    
    def actualizartemperatura(self, accion):
        # Modifica el estado según la acción
        if accion == "enfriar":
            self.temperatura -= 1
        elif accion == "calentar":
            self.temperatura += 1
        # "esperar" no modifica la temperatura
        return self.temperatura
```

### Clase Agente

```python
class Agente:
    def accion(self, temperatura):
        # Lógica f(estado) del agente reflejo simple
        if temperatura < 18:
            return "calentar"
        elif temperatura > 25:
            return "enfriar"
        else:
            return "esperar"
```
