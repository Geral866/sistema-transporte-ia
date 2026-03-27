# sistema-transporte-ia# Sistema Inteligente de Transporte Masivo

## 📄 Descripción
Este proyecto es un sistema inteligente basado en conocimiento diseñado para calcular la mejor ruta entre dos puntos (Estación A y Estación B) en una red de transporte masivo local. 

El sistema utiliza **lógica simbólica** para representar el conocimiento de la red y **algoritmos de búsqueda heurística** para optimizar el trayecto, permitiendo también la gestión de restricciones dinámicas (como estaciones cerradas).

## 📚 Marco Teórico
El desarrollo de este sistema se basa en los fundamentos de Inteligencia Artificial presentados en:
> **Benítez, R. (2014). Inteligencia artificial avanzada. Barcelona: Editorial UOC.**

Específicamente se aplican los conceptos de:
*   **Capítulo 2:** Lógica y representación del conocimiento (Hechos y Predicados).
*   **Capítulo 3:** Sistemas basados en reglas (Restricciones de estaciones).
*   **Capítulo 9:** Técnicas basadas en búsquedas heurísticas (Algoritmo A*).

## 🚀 Características
*   **Búsqueda Óptima:** Encuentra el camino de menor costo utilizando el algoritmo A*.
*   **Base de Conocimiento:** Representación de la red de transporte mediante grafos en Python.
*   **Reglas Dinámicas:** Capacidad para simular cierres de estaciones y recalcular rutas en tiempo real.
*   **Interfaz Consola:** Menú interactivo fácil de usar para pruebas.

## 🛠️ Requisitos
*   Python 3.x instalado.
*   No se requieren librerías externas (solo librerías estándar como `heapq`).

## 📂 Estructura del Proyecto
*   `knowledge_base.py`: Contiene la representación del conocimiento (grafo) y las reglas lógicas.
*   `search_engine.py`: Implementa el motor de inferencia y el algoritmo de búsqueda A*.
*   `main.py`: Punto de entrada del programa e interfaz de usuario.
*   `README.md`: Este archivo de documentación.

## ▶️ Instrucciones de Ejecución
1.  Clonar o descargar el repositorio.
2.  Abrir una terminal en la carpeta del proyecto.
3.  Ejecutar el siguiente comando:
    ```bash
    python main.py
    ```
4.  Seguir las instrucciones del menú en pantalla.

## 🧪 Pruebas Realizadas
Se realizaron pruebas de funcionamiento para validar:
1.  Cálculo de ruta óptima en condiciones normales.
2.  Recalculo de ruta ante la aplicación de reglas (estaciones cerradas).
3.  Validación de entradas de usuario.

*(Ver documento PDF adjunto para evidencias detalladas)*

## 👤 Autor
*   **Estudiante:** YERALDIN ARBOLEDA QUINTERO
*   **Curso:** Inteligencia Artificial
*   **Fecha:** 2024

## 📄 Licencia
Este proyecto es de uso académico.
