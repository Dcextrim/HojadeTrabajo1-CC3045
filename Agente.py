#Universidad del Valle de Guatemala
#Inteligencia Aritificial - CC3045 - Sección 10
#Hoja de Trabajo 1
#Fecha 18/01/2026
#Daniel Chet - 231177
#Dulce Ambrosio - 231143

class Agente:
        
    def accion(self, temperatura):
            #Si es menor a 18 grados, calentar
            if temperatura < 18:
                return "calentar"
            #Si es mayor a 25 grados, enfriar
            elif temperatura > 25:
                return "enfriar"
            # Si está entre 18 y 25 grados, esperar
            else:
                return "esperar"
            
