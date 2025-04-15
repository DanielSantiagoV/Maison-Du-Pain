from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime
import json
import os

console = Console()

def cargar_pedidos():
    """Carga los pedidos desde el archivo JSON"""
    try:
        with open("datos/pedidos/pedidos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"pedidos": []}

def cargar_detalles_pedidos():
    """Carga los detalles de pedidos desde el archivo JSON"""
    try:
        with open("datos/pedidos/detalles_pedidos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"detalles_pedidos": []}