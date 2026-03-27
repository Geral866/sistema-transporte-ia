# knowledge_base.py
# Representación del Conocimiento (Capítulo 2 y 3 - Benítez)

class BaseConocimiento:
    def __init__(self):
        # Hechos: Grafo del transporte (Diccionario de adyacencia con costos)
        # Formato: Estacion: {Vecino: Costo, ...}
        self.red_transporte = {
            'A': {'B': 5, 'C': 2},
            'B': {'A': 5, 'D': 4, 'E': 2},
            'C': {'A': 2, 'D': 8, 'F': 3},
            'D': {'B': 4, 'C': 8, 'G': 6, 'F': 1},
            'E': {'B': 2, 'G': 3},
            'F': {'C': 3, 'D': 1, 'H': 4},
            'G': {'D': 6, 'E': 3, 'I': 5},
            'H': {'F': 4, 'I': 2},
            'I': {'G': 5, 'H': 2, 'J': 3},
            'J': {'I': 3}
        }
        
        # Reglas de Negocio (Sistema Basado en Reglas)
        # Ejemplo: Estaciones en mantenimiento
        self.estaciones_cerradas = [] 

    def obtener_vecinos(self, estacion):
        """Obtiene las conexiones lógicas permitidas"""
        if estacion not in self.red_transporte:
            return []
        
        vecinos_validos = []
        for vecino, costo in self.red_transporte[estacion].items():
            # Aplicación de Regla: Si está cerrada, no es un vecino válido
            if vecino not in self.estaciones_cerradas:
                vecinos_validos.append((vecino, costo))
            else:
                print(f"[Regla] Estación {vecino} omitida por mantenimiento.")
        return vecinos_validos

    def heuristic(self, estacion, meta):
        """
        Heurística (Capítulo 9): Distancia estimada.
        Para este ejemplo, usamos una distancia simplificada (pueden usar coordenadas reales).
        """
        # Valores ficticios de distancia en línea recta a la meta 'J'
        distancias_aproximadas = {
            'A': 15, 'B': 12, 'C': 13, 'D': 10, 'E': 11,
            'F': 9, 'G': 7, 'H': 5, 'I': 3, 'J': 0
        }
        return distancias_aproximadas.get(estacion, 999)

    def cerrar_estacion(self, nombre):
        self.estaciones_cerradas.append(nombre)
        print(f"[Sistema] Regla actualizada: {nombre} ahora está cerrada.")