# search_engine.py
# Técnicas de Búsqueda Heurística (Capítulo 9 - Benítez)

import heapq

class MotorBusqueda:
    def __init__(self, base_conocimiento):
        self.bc = base_conocimiento

    def buscar_ruta_a_estrella(self, inicio, meta):
        """
        Implementación del algoritmo A*
        Retorna: (camino, costo_total) o (None, inf) si no hay ruta
        """
        # Cola de prioridad: (f_score, g_score, estacion_actual, camino)
        # f = g + h
        abierto = []
        heapq.heappush(abierto, (0, 0, inicio, [inicio]))
        
        visitado = set()
        g_scores = {inicio: 0}

        while abierto:
            f, g, actual, camino = heapq.heappop(abierto)

            if actual == meta:
                return camino, g

            if actual in visitado:
                continue
            visitado.add(actual)

            # Obtener vecinos basados en las reglas de la Base de Conocimiento
            vecinos = self.bc.obtener_vecinos(actual)

            for vecino, costo_arista in vecinos:
                nuevo_g = g + costo_arista
                
                if vecino not in g_scores or nuevo_g < g_scores[vecino]:
                    g_scores[vecino] = nuevo_g
                    h = self.bc.heuristic(vecino, meta)
                    f = nuevo_g + h
                    nuevo_camino = camino + [vecino]
                    heapq.heappush(abierto, (f, nuevo_g, vecino, nuevo_camino))

        return None, float('inf')