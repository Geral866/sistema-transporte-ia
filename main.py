# main.py
# Punto de entrada del Sistema Inteligente

from knowledge_base import BaseConocimiento
from search_engine import MotorBusqueda

def main():
    print("=== SISTEMA INTELIGENTE DE TRANSPORTE MASIVO ===")
    print("Basado en Reglas y Búsqueda Heurística (A*)")
    
    # Inicialización
    bc = BaseConocimiento()
    motor = MotorBusqueda(bc)

    while True:
        print("\nOpciones:")
        print("1. Buscar Ruta")
        print("2. Simular Falla (Cerrar Estación)")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            inicio = input("Estación de Origen (Ej: A): ").upper()
            meta = input("Estación de Destino (Ej: J): ").upper()
            
            camino, costo = motor.buscar_ruta_a_estrella(inicio, meta)
            
            if camino:
                print(f"\n[Éxito] Ruta óptima encontrada: {' -> '.join(camino)}")
                print(f"[Costo] Tiempo/Distance total: {costo}")
            else:
                print("\n[Error] No se encontró ruta posible con las reglas actuales.")
                
        elif opcion == '2':
            est = input("Nombre de estación a cerrar: ").upper()
            bc.cerrar_estacion(est)
            
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
    