"""
Punto de entrada principal del simulador DSKY
"""

from src.core import DSKYCore
from src.gui import DSKYGUI

def main():
    """Función principal que inicia el simulador DSKY"""
    # Crear instancia de la lógica core
    dsky_core = DSKYCore()
    
    # Crear y configurar la interfaz gráfica
    gui = DSKYGUI(dsky_core.ejecutar_comando)
    gui.crear_interfaz()
    
    # Iniciar la aplicación
    gui.iniciar()

if __name__ == "__main__":
    main()
