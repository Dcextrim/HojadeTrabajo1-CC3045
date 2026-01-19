#Universidad del Valle de Guatemala
#Inteligencia Aritificial - CC3045 - Sección 10
#Hoja de Trabajo 1
#Fecha 18/01/2026
#Daniel Chet - 231177
#Dulce Ambrosio - 231143

from Ambiente import Ambiente
from Agente import Agente

Ambiente1 = Ambiente()
Agente1 = Agente()

for i in range(10):
    # Obtener la temperatura actual del ambiente
    sensor = Ambiente1.obtenertemperatura()
    # Obtener la acción del agente basada en la temperatura actual
    accion = Agente1.accion(sensor)
    # Actualizar la temperatura del ambiente según la acción del agente
    nuevatemperatura = Ambiente1.actualizartemperatura(accion)
    # Imprimir el estado actual
    print("Temperatura actual:", sensor, "°C - Acción del agente:", accion, "- Nueva temperatura:", nuevatemperatura, "°C")