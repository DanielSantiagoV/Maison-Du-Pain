"""
Módulo de configuración del sistema
Maneja configuraciones globales y preferencias del usuario
"""
import json
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Ruta del archivo de configuración
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, "config", "config.json")

# Configuración por defecto
CONFIG_DEFAULT = {
    "sistema": {
        "nombre_empresa": "Maison du Pain",
        "version": "2.0.0",
        "idioma": "es",
        "zona_horaria": "America/Bogota"
    },
    "inventario": {
        "stock_minimo": 5,
        "stock_critico": 2,
        "alertas_automaticas": True,
        "respaldo_automatico": True,
        "dias_retener_respaldos": 30
    },
    "ventas": {
        "moneda": "COP",
        "decimales": 2,
        "impuestos": 0.19,
        "descuento_maximo": 0.15
    },
    "interfaz": {
        "colores": True,
        "emojis": True,
        "tablas_detalladas": True,
        "confirmaciones": True
    },
    "reportes": {
        "exportar_automatico": False,
        "formato_exportacion": "json",
        "incluir_detalles": True
    }
}

def cargar_configuracion():
    """Carga la configuración desde el archivo"""
    try:
        # Crear directorio de configuración si no existe
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                config = json.load(f)
                # Combinar con configuración por defecto para campos faltantes
                return combinar_configuraciones(CONFIG_DEFAULT, config)
        else:
            # Crear archivo de configuración por defecto
            guardar_configuracion(CONFIG_DEFAULT)
            return CONFIG_DEFAULT
    except Exception as e:
        console.print(f"[bold red]Error al cargar configuración: {e}[/bold red]")
        return CONFIG_DEFAULT

def guardar_configuracion(config):
    """Guarda la configuración en el archivo"""
    try:
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        console.print(f"[bold red]Error al guardar configuración: {e}[/bold red]")
        return False

def combinar_configuraciones(default, user):
    """Combina configuración por defecto con configuración del usuario"""
    result = default.copy()
    
    def merge_dicts(d1, d2):
        for key, value in d2.items():
            if key in d1 and isinstance(d1[key], dict) and isinstance(value, dict):
                merge_dicts(d1[key], value)
            else:
                d1[key] = value
    
    merge_dicts(result, user)
    return result

def mostrar_menu_configuracion():
    """Muestra el menú de configuración"""
    console.print("\n[bold cyan]=== ⚙️ CONFIGURACIÓN DEL SISTEMA ===[/bold cyan]")
    console.print("1️⃣ 📋 Ver Configuración Actual")
    console.print("2️⃣ 🏢 Configurar Empresa")
    console.print("3️⃣ 📦 Configurar Inventario")
    console.print("4️⃣ 💰 Configurar Ventas")
    console.print("5️⃣ 🎨 Configurar Interfaz")
    console.print("6️⃣ 📊 Configurar Reportes")
    console.print("7️⃣ 🔄 Restaurar Configuración por Defecto")
    console.print("8️⃣ 🔙 Volver al Menú Principal")
    return input("\n⚡ Seleccione una opción: ")

def mostrar_configuracion_actual(config):
    """Muestra la configuración actual en formato de tabla"""
    console.print("\n[bold green]=== CONFIGURACIÓN ACTUAL ===[/bold green]")
    
    # Sistema
    tabla_sistema = Table(title="🏢 Configuración del Sistema")
    tabla_sistema.add_column("Parámetro", style="cyan", justify="center")
    tabla_sistema.add_column("Valor", style="green", justify="center")
    
    for key, value in config["sistema"].items():
        tabla_sistema.add_row(key.replace("_", " ").title(), str(value))
    
    console.print(tabla_sistema)
    
    # Inventario
    tabla_inventario = Table(title="📦 Configuración de Inventario")
    tabla_inventario.add_column("Parámetro", style="cyan", justify="center")
    tabla_inventario.add_column("Valor", style="green", justify="center")
    
    for key, value in config["inventario"].items():
        tabla_inventario.add_row(key.replace("_", " ").title(), str(value))
    
    console.print(tabla_inventario)
    
    # Ventas
    tabla_ventas = Table(title="💰 Configuración de Ventas")
    tabla_ventas.add_column("Parámetro", style="cyan", justify="center")
    tabla_ventas.add_column("Valor", style="green", justify="center")
    
    for key, value in config["ventas"].items():
        tabla_ventas.add_row(key.replace("_", " ").title(), str(value))
    
    console.print(tabla_ventas)

def configurar_empresa(config):
    """Configura los parámetros de la empresa"""
    console.print("\n[bold green]=== CONFIGURACIÓN DE EMPRESA ===[/bold green]")
    
    config["sistema"]["nombre_empresa"] = input(f"Nombre de la empresa [{config['sistema']['nombre_empresa']}]: ") or config["sistema"]["nombre_empresa"]
    config["sistema"]["idioma"] = input(f"Idioma (es/en) [{config['sistema']['idioma']}]: ") or config["sistema"]["idioma"]
    config["sistema"]["zona_horaria"] = input(f"Zona horaria [{config['sistema']['zona_horaria']}]: ") or config["sistema"]["zona_horaria"]
    
    if guardar_configuracion(config):
        console.print("\n[bold green]✅ Configuración de empresa actualizada[/bold green]")
    else:
        console.print("\n[bold red]❌ Error al guardar configuración[/bold red]")

def configurar_inventario(config):
    """Configura los parámetros de inventario"""
    console.print("\n[bold green]=== CONFIGURACIÓN DE INVENTARIO ===[/bold green]")
    
    try:
        stock_min = input(f"Stock mínimo [{config['inventario']['stock_minimo']}]: ")
        if stock_min:
            config["inventario"]["stock_minimo"] = int(stock_min)
        
        stock_critico = input(f"Stock crítico [{config['inventario']['stock_critico']}]: ")
        if stock_critico:
            config["inventario"]["stock_critico"] = int(stock_critico)
        
        alertas = input(f"Alertas automáticas (s/n) [{'s' if config['inventario']['alertas_automaticas'] else 'n'}]: ")
        if alertas.lower() in ['s', 'si', 'sí', 'y', 'yes']:
            config["inventario"]["alertas_automaticas"] = True
        elif alertas.lower() in ['n', 'no']:
            config["inventario"]["alertas_automaticas"] = False
        
        respaldo = input(f"Respaldo automático (s/n) [{'s' if config['inventario']['respaldo_automatico'] else 'n'}]: ")
        if respaldo.lower() in ['s', 'si', 'sí', 'y', 'yes']:
            config["inventario"]["respaldo_automatico"] = True
        elif respaldo.lower() in ['n', 'no']:
            config["inventario"]["respaldo_automatico"] = False
        
        dias = input(f"Días a retener respaldos [{config['inventario']['dias_retener_respaldos']}]: ")
        if dias:
            config["inventario"]["dias_retener_respaldos"] = int(dias)
        
        if guardar_configuracion(config):
            console.print("\n[bold green]✅ Configuración de inventario actualizada[/bold green]")
        else:
            console.print("\n[bold red]❌ Error al guardar configuración[/bold red]")
    except ValueError:
        console.print("\n[bold red]❌ Error: Ingrese valores numéricos válidos[/bold red]")

def configurar_ventas(config):
    """Configura los parámetros de ventas"""
    console.print("\n[bold green]=== CONFIGURACIÓN DE VENTAS ===[/bold green]")
    
    try:
        config["ventas"]["moneda"] = input(f"Moneda [{config['ventas']['moneda']}]: ") or config["ventas"]["moneda"]
        
        decimales = input(f"Decimales [{config['ventas']['decimales']}]: ")
        if decimales:
            config["ventas"]["decimales"] = int(decimales)
        
        impuestos = input(f"Impuestos (0.0-1.0) [{config['ventas']['impuestos']}]: ")
        if impuestos:
            config["ventas"]["impuestos"] = float(impuestos)
        
        descuento = input(f"Descuento máximo (0.0-1.0) [{config['ventas']['descuento_maximo']}]: ")
        if descuento:
            config["ventas"]["descuento_maximo"] = float(descuento)
        
        if guardar_configuracion(config):
            console.print("\n[bold green]✅ Configuración de ventas actualizada[/bold green]")
        else:
            console.print("\n[bold red]❌ Error al guardar configuración[/bold red]")
    except ValueError:
        console.print("\n[bold red]❌ Error: Ingrese valores numéricos válidos[/bold red]")

def configurar_interfaz(config):
    """Configura los parámetros de la interfaz"""
    console.print("\n[bold green]=== CONFIGURACIÓN DE INTERFAZ ===[/bold green]")
    
    colores = input(f"Usar colores (s/n) [{'s' if config['interfaz']['colores'] else 'n'}]: ")
    if colores.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        config["interfaz"]["colores"] = True
    elif colores.lower() in ['n', 'no']:
        config["interfaz"]["colores"] = False
    
    emojis = input(f"Usar emojis (s/n) [{'s' if config['interfaz']['emojis'] else 'n'}]: ")
    if emojis.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        config["interfaz"]["emojis"] = True
    elif emojis.lower() in ['n', 'no']:
        config["interfaz"]["emojis"] = False
    
    tablas = input(f"Tablas detalladas (s/n) [{'s' if config['interfaz']['tablas_detalladas'] else 'n'}]: ")
    if tablas.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        config["interfaz"]["tablas_detalladas"] = True
    elif tablas.lower() in ['n', 'no']:
        config["interfaz"]["tablas_detalladas"] = False
    
    confirmaciones = input(f"Confirmaciones (s/n) [{'s' if config['interfaz']['confirmaciones'] else 'n'}]: ")
    if confirmaciones.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        config["interfaz"]["confirmaciones"] = True
    elif confirmaciones.lower() in ['n', 'no']:
        config["interfaz"]["confirmaciones"] = False
    
    if guardar_configuracion(config):
        console.print("\n[bold green]✅ Configuración de interfaz actualizada[/bold green]")
    else:
        console.print("\n[bold red]❌ Error al guardar configuración[/bold red]")

def configurar_reportes(config):
    """Configura los parámetros de reportes"""
    console.print("\n[bold green]=== CONFIGURACIÓN DE REPORTES ===[/bold green]")
    
    exportar = input(f"Exportación automática (s/n) [{'s' if config['reportes']['exportar_automatico'] else 'n'}]: ")
    if exportar.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        config["reportes"]["exportar_automatico"] = True
    elif exportar.lower() in ['n', 'no']:
        config["reportes"]["exportar_automatico"] = False
    
    formato = input(f"Formato de exportación (json/csv) [{config['reportes']['formato_exportacion']}]: ")
    if formato.lower() in ['json', 'csv']:
        config["reportes"]["formato_exportacion"] = formato.lower()
    
    detalles = input(f"Incluir detalles (s/n) [{'s' if config['reportes']['incluir_detalles'] else 'n'}]: ")
    if detalles.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        config["reportes"]["incluir_detalles"] = True
    elif detalles.lower() in ['n', 'no']:
        config["reportes"]["incluir_detalles"] = False
    
    if guardar_configuracion(config):
        console.print("\n[bold green]✅ Configuración de reportes actualizada[/bold green]")
    else:
        console.print("\n[bold red]❌ Error al guardar configuración[/bold red]")

def restaurar_configuracion_por_defecto():
    """Restaura la configuración por defecto"""
    console.print("\n[bold yellow]⚠ ¿Está seguro de que desea restaurar la configuración por defecto?[/bold yellow]")
    confirmacion = input("Esta acción no se puede deshacer (s/n): ")
    
    if confirmacion.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        if guardar_configuracion(CONFIG_DEFAULT):
            console.print("\n[bold green]✅ Configuración restaurada por defecto[/bold green]")
            return CONFIG_DEFAULT
        else:
            console.print("\n[bold red]❌ Error al restaurar configuración[/bold red]")
            return cargar_configuracion()
    else:
        console.print("\n[bold blue]Operación cancelada[/bold blue]")
        return cargar_configuracion()

def gestionar_configuracion():
    """Función principal para gestionar la configuración"""
    config = cargar_configuracion()
    
    while True:
        opcion = mostrar_menu_configuracion()
        
        if opcion == "1":
            mostrar_configuracion_actual(config)
        elif opcion == "2":
            configurar_empresa(config)
        elif opcion == "3":
            configurar_inventario(config)
        elif opcion == "4":
            configurar_ventas(config)
        elif opcion == "5":
            configurar_interfaz(config)
        elif opcion == "6":
            configurar_reportes(config)
        elif opcion == "7":
            config = restaurar_configuracion_por_defecto()
        elif opcion == "8":
            break
        else:
            console.print("\n[bold yellow]⚠ Opción no válida[/bold yellow]")
        
        if opcion != "8":
            input("\n⏸️ Presione Enter para continuar...")
    
    return config 