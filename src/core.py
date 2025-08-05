"""
Módulo core del simulador DSKY
Contiene la lógica de comandos y funcionalidad principal
"""

class DSKYCore:
    """Clase principal que maneja la lógica del simulador DSKY"""
    
    def __init__(self):
        # Diccionario de comandos VERB-NOUN
       self.comandos = {
        ('06', '20'): " Mostrando velocidad (X, Y, Z)...",
        ('16', '36'): " Mostrando orientación (pitch, roll, yaw)...",
        ('37', '63'): " Iniciando programa automático de navegación...",
        ('06', '17'): " Altitud sobre superficie lunar: 3200m",
        ('27', '10'): " Navegación estelar activada. Localizando estrellas guía...",
        ('41', '18'): " Iniciando secuencia de descenso lunar...",
        ('91', '01'): " Iniciando música de la Tierra... [Fly me to the Moon]",
        ('54', '77'): " Transmitiendo mensaje: 'Houston, todo bajo control.'",
    }

    
    def ejecutar_comando(self, verb: str, noun: str) -> str:
        """
        Ejecuta un comando VERB-NOUN
        
        Args:
            verb: Código de acción (2 dígitos)
            noun: Código de dato (2 dígitos)
            
        Returns:
            str: Resultado del comando o mensaje de error
        """
        # Normalizar entradas a 2 dígitos
        verb_norm = verb.zfill(2)
        noun_norm = noun.zfill(2)
        
        # Buscar comando en el diccionario
        resultado = self.comandos.get((verb_norm, noun_norm), "Comando no reconocido.")
        return resultado
    
    def limpiar_entradas(self) -> tuple:
        """
        Retorna valores limpios para las entradas
        
        Returns:
            tuple: (verb_limpio, noun_limpio)
        """
        return ("", "")
    
    def validar_entrada(self, valor: str) -> bool:
        """
        Valida que la entrada sea numérica y de máximo 2 dígitos
        
        Args:
            valor: Valor a validar
            
        Returns:
            bool: True si es válido, False en caso contrario
        """
        if not valor:
            return True  # Campo vacío es válido
        
        try:
            int_valor = int(valor)
            return 0 <= int_valor <= 99
        except ValueError:
            return False
