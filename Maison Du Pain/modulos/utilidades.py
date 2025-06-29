"""
Módulo de utilidades del sistema
Funciones auxiliares y herramientas para el sistema de panadería
"""
import os
import json
import csv
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def validar_entrada_numerica(mensaje, valor_minimo=None, valor_maximo=None):
    """Valida entrada numérica del usuario"""
    while True:
        try:
            valor = input(mensaje)
            numero = float(valor)
            
            if valor_minimo is not None and numero < valor_minimo:
                console.print(f"[bold red]❌ El valor debe ser mayor o igual a {valor_minimo}[/bold red]")
                continue
                
            if valor_maximo is not None and numero > valor_maximo:
                console.print(f"[bold red]❌ El valor debe ser menor o igual a {valor_maximo}[/bold red]")
                continue
                
            return numero
        except ValueError:
            console.print("[bold red]❌ Por favor, ingrese un número válido[/bold red]")

def validar_entrada_entera(mensaje, valor_minimo=None, valor_maximo=None):
    """Valida entrada de números enteros del usuario"""
    while True:
        try:
            valor = input(mensaje)
            numero = int(valor)
            
            if valor_minimo is not None and numero < valor_minimo:
                console.print(f"[bold red]❌ El valor debe ser mayor o igual a {valor_minimo}[/bold red]")
                continue
                
            if valor_maximo is not None and numero > valor_maximo:
                console.print(f"[bold red]❌ El valor debe ser menor o igual a {valor_maximo}[/bold red]")
                continue
                
            return numero
        except ValueError:
            console.print("[bold red]❌ Por favor, ingrese un número entero válido[/bold red]")

def confirmar_accion(mensaje="¿Está seguro de continuar?"):
    """Solicita confirmación del usuario"""
    respuesta = input(f"{mensaje} (s/n): ").lower()
    return respuesta in ['s', 'si', 'sí', 'y', 'yes']

def formatear_moneda(valor, moneda="COP"):
    """Formatea un valor como moneda"""
    return f"{moneda} ${valor:,.2f}"

def formatear_fecha(fecha_str):
    """Formatea una fecha en formato legible"""
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        return fecha.strftime("%d/%m/%Y %H:%M")
    except:
        return fecha_str

def calcular_edad_dias(fecha_str):
    """Calcula la edad en días de una fecha"""
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        return (datetime.now() - fecha).days
    except:
        return 0

def exportar_a_csv(datos, nombre_archivo, campos):
    """Exporta datos a formato CSV"""
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(datos)
        return True
    except Exception as e:
        console.print(f"[bold red]Error al exportar CSV: {e}[/bold red]")
        return False

def generar_reporte_texto(datos, titulo):
    """Genera un reporte en formato de texto plano"""
    reporte = f"""
{'='*50}
{titulo}
{'='*50}
Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

"""
    
    if isinstance(datos, list):
        for i, item in enumerate(datos, 1):
            reporte += f"{i}. {item}\n"
    elif isinstance(datos, dict):
        for key, value in datos.items():
            reporte += f"{key}: {value}\n"
    
    return reporte

def guardar_reporte_texto(reporte, nombre_archivo):
    """Guarda un reporte en formato texto"""
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(reporte)
        return True
    except Exception as e:
        console.print(f"[bold red]Error al guardar reporte: {e}[/bold red]")
        return False

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_progreso(descripcion, total=100):
    """Muestra una barra de progreso"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(descripcion, total=total)
        return task, progress

def validar_email(email):
    """Valida formato básico de email"""
    import re
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_telefono(telefono):
    """Valida formato básico de teléfono"""
    import re
    # Eliminar espacios, guiones y paréntesis
    telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono)
    # Verificar que solo contenga números y tenga longitud válida
    return telefono_limpio.isdigit() and len(telefono_limpio) >= 7

def generar_codigo_aleatorio(longitud=8):
    """Genera un código aleatorio alfanumérico"""
    import random
    import string
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def calcular_margen_ganancia(precio_venta, precio_costo):
    """Calcula el margen de ganancia en porcentaje"""
    if precio_costo == 0:
        return 0
    return ((precio_venta - precio_costo) / precio_costo) * 100

def calcular_precio_con_impuesto(precio, tasa_impuesto=0.19):
    """Calcula el precio con impuestos incluidos"""
    return precio * (1 + tasa_impuesto)

def calcular_precio_sin_impuesto(precio_con_impuesto, tasa_impuesto=0.19):
    """Calcula el precio sin impuestos"""
    return precio_con_impuesto / (1 + tasa_impuesto)

def redondear_moneda(valor, decimales=2):
    """Redondea un valor monetario"""
    return round(valor, decimales)

def obtener_estadisticas_rapidas(datos_productos):
    """Obtiene estadísticas rápidas de los productos"""
    if not datos_productos["productos"]:
        return {}
    
    total_productos = len(datos_productos["productos"])
    total_stock = sum(p["cantidad_en_stock"] for p in datos_productos["productos"])
    valor_inventario = sum(p["cantidad_en_stock"] * p["precio_venta"] for p in datos_productos["productos"])
    productos_stock_bajo = len([p for p in datos_productos["productos"] if p["cantidad_en_stock"] < 5])
    
    # Categorías
    categorias = {}
    for producto in datos_productos["productos"]:
        cat = producto["categoria"]
        if cat not in categorias:
            categorias[cat] = {"cantidad": 0, "valor": 0}
        categorias[cat]["cantidad"] += 1
        categorias[cat]["valor"] += producto["cantidad_en_stock"] * producto["precio_venta"]
    
    return {
        "total_productos": total_productos,
        "total_stock": total_stock,
        "valor_inventario": valor_inventario,
        "productos_stock_bajo": productos_stock_bajo,
        "categorias": categorias
    }

def mostrar_tabla_estadisticas(stats):
    """Muestra estadísticas en formato de tabla"""
    tabla = Table(title="📊 Estadísticas Rápidas")
    tabla.add_column("Métrica", style="cyan", justify="center")
    tabla.add_column("Valor", style="green", justify="center")
    
    tabla.add_row("Total Productos", str(stats["total_productos"]))
    tabla.add_row("Total en Stock", str(stats["total_stock"]))
    tabla.add_row("Valor Inventario", formatear_moneda(stats["valor_inventario"]))
    tabla.add_row("Productos Stock Bajo", str(stats["productos_stock_bajo"]))
    
    console.print(tabla)
    
    # Mostrar categorías
    if stats["categorias"]:
        tabla_cat = Table(title="🏷️ Por Categoría")
        tabla_cat.add_column("Categoría", style="cyan", justify="center")
        tabla_cat.add_column("Cantidad", style="green", justify="center")
        tabla_cat.add_column("Valor", style="yellow", justify="center")
        
        for categoria, datos in stats["categorias"].items():
            tabla_cat.add_row(
                categoria.title(),
                str(datos["cantidad"]),
                formatear_moneda(datos["valor"])
            )
        
        console.print(tabla_cat)

def crear_directorio_si_no_existe(ruta):
    """Crea un directorio si no existe"""
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        return True
    return False

def obtener_tamaño_archivo(ruta_archivo):
    """Obtiene el tamaño de un archivo en bytes"""
    try:
        return os.path.getsize(ruta_archivo)
    except:
        return 0

def formatear_tamaño_archivo(bytes):
    """Formatea el tamaño de archivo en formato legible"""
    for unidad in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.1f} {unidad}"
        bytes /= 1024.0
    return f"{bytes:.1f} TB" 