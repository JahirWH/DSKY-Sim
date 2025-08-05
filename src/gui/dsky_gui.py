"""
Módulo de interfaz gráfica del simulador DSKY
Maneja toda la interfaz de usuario
"""

import tkinter as tk
from tkinter import messagebox
from typing import Callable

class DSKYGUI:
    """Clase que maneja la interfaz gráfica del simulador DSKY"""
    
    def __init__(self, core_logic: Callable):
        """
        Inicializa la interfaz gráfica
        
        Args:
            core_logic: Función que maneja la lógica de comandos
        """
        self.core_logic = core_logic
        self.root = None
        self.verb_entry = None
        self.noun_entry = None
        self.resultado_label = None
        
    def crear_interfaz(self):
        """Crea y configura la interfaz gráfica"""
        # Ventana principal
        self.root = tk.Tk()
        self.root.title("Simulador DSKY (Apollo)")
        
        # Configurar grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        
        # Crear widgets
        self._crear_campos_entrada()
        self._crear_botones()
        self._crear_resultado()
        
        # Configurar estética
        self.root.configure(padx=30, pady=30)
        
    def _crear_campos_entrada(self):
        """Crea los campos de entrada VERB y NOUN"""
        # Campo VERB
        tk.Label(self.root, text="VERB (acción):", font=("Arial", 10, "bold")).grid(
            row=0, column=0, sticky="e", padx=5, pady=5
        )
        self.verb_entry = tk.Entry(self.root, width=5, font=("Courier", 12))
        self.verb_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Campo NOUN
        tk.Label(self.root, text="NOUN (dato):", font=("Arial", 10, "bold")).grid(
            row=1, column=0, sticky="e", padx=5, pady=5
        )
        self.noun_entry = tk.Entry(self.root, width=5, font=("Courier", 12))
        self.noun_entry.grid(row=1, column=1, padx=5, pady=5)
        
    def _crear_botones(self):
        """Crea los botones de la interfaz"""
        # Botones VERB y NOUN
        verb_btn = tk.Button(
            self.root, 
            text="VERB", 
            command=self._limpiar_entradas,
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="raised"
        )
        verb_btn.grid(row=0, column=2, padx=10, pady=5)
        
        noun_btn = tk.Button(
            self.root, 
            text="NOUN", 
            command=self._limpiar_entradas,
            font=("Arial", 10, "bold"),
            bg="#2196F3",
            fg="white",
            relief="raised"
        )
        noun_btn.grid(row=1, column=2, padx=10, pady=5)
        
        # Botón ENTR
        ejecutar_btn = tk.Button(
            self.root, 
            text="ENTR", 
            command=self._ejecutar_comando,
            font=("Arial", 12, "bold"),
            bg="#FF9800",
            fg="white",
            relief="raised",
            width=10
        )
        ejecutar_btn.grid(row=2, column=0, columnspan=2, pady=20)
        
    def _crear_resultado(self):
        """Crea el área de resultado"""
        self.resultado_label = tk.Label(
            self.root, 
            text="Resultado aparecerá aquí", 
            fg="green", 
            font=("Courier", 12),
            bg="black",
            relief="sunken",
            width=40,
            height=3
        )
        self.resultado_label.grid(row=3, column=0, columnspan=3, pady=20)
        
    def _ejecutar_comando(self):
        """Ejecuta el comando ingresado"""
        verb = self.verb_entry.get()
        noun = self.noun_entry.get()
        
        # Validar entradas
        if not verb or not noun:
            messagebox.showwarning("Advertencia", "Por favor ingrese VERB y NOUN")
            return
            
        # Ejecutar comando
        resultado = self.core_logic(verb, noun)
        self.resultado_label.config(text=resultado)
        
    def _limpiar_entradas(self):
        """Limpia los campos de entrada"""
        self.verb_entry.delete(0, tk.END)
        self.noun_entry.delete(0, tk.END)
        self.resultado_label.config(text="Resultado aparecerá aquí")
        
    def iniciar(self):
        """Inicia la aplicación"""
        if self.root:
            self.root.mainloop()
