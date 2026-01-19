#Universidad del Valle de Guatemala
#Inteligencia Aritificial - CC3045 - Sección 10
#Hoja de Trabajo 1
#Fecha 18/01/2026
#Daniel Chet - 231177
#Dulce Ambrosio - 231143

from random import *

class Ambiente:
    def __init__(self):
        # Temperatura inicial aleatoria entre 10 y 30 grados Celsius
        self.temperatura = randint(10, 30)  
    
    # Simula la obtención de la temperatura ambiente y retorna el valor en grados Celsius
    def obtenertemperatura(self):
        grados = self.temperatura
        return grados
    
    # Actualiza la temperatura según la acción recibida del agente: "enfriar", "calentar" o "esperar"
    def  actualizartemperatura(self, accion):
        if accion == "enfriar":
            # Si la acción es enfriar, resta a la temperatura 1 grado
            self.temperatura = self.temperatura - 1 
        elif accion == "calentar":
            # Si la acción es calentar, suma a la temperatura 1 grado
            self.temperatura = self.temperatura + 1 
        elif accion == "esperar":
            # Si la accion es esperar, no se realiza ningún cambio en la temperatura
            pass  

        return self.temperatura