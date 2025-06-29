"""
Sistema de Gestión de Panadería "Maison du Pain"
Archivo principal para la ejecución del programa
Versión 2.0.0 - Mejorada con reportes, configuración y respaldos
"""
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from datetime import datetime

from modulos.gestion_archivos import cargar_datos, guardar_datos
from modulos.gestion_productos import gestionar_productos
from modulos.gestion_pedidos import gestionar_pedidos
from modulos.reportes import gestionar_reportes
from modulos.configuracion import gestionar_configuracion, cargar_configuracion

# Instancia de consola para la visualización
console = Console()

def mostrar_banner():
    """Muestra un banner ASCII con el nombre de la panadería"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║  ███╗   ███╗ █████╗ ██╗███████╗ ██████╗ ███╗   ██╗          ║
    ║  ████╗ ████║██╔══██╗██║██╔════╝██╔═══██╗████╗  ██║          ║
    ║  ██╔████╔██║███████║██║███████╗██║   ██║██╔██╗ ██║          ║
    ║  ██║╚██╔╝██║██╔══██║██║╚════██║██║   ██║██║╚██╗██║          ║
    ║  ██║ ╚═╝ ██║██║  ██║██║███████║╚██████╔╝██║ ╚████║          ║
    ║  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝          ║
    ║                                                              ║
    ║    ██████╗ ██╗   ██╗    ██████╗  █████╗ ██╗███╗   ██╗       ║
    ║    ██╔══██╗██║   ██║    ██╔══██╗██╔══██╗██║████╗  ██║       ║
    ║    ██║  ██║██║   ██║    ██████╔╝███████║██║██╔██╗ ██║       ║
    ║    ██║  ██║██║   ██║    ██╔═══╝ ██╔══██║██║██║╚██╗██║       ║
    ║    ██████╔╝╚██████╔╝    ██║     ██║  ██║██║██║ ╚████║       ║
    ║    ╚═════╝  ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝       ║
    ║                                                              ║
    ║           Sistema de Gestión de Panadería v2.0.0            ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    
    # Creamos un texto con el banner y lo mostramos en rojo
    text = Text(banner, style="bold red", justify="center")
    console.print(Panel(text, 
                       title="🥐 Bienvenido 🥖", 
                       subtitle="🍰 Sistema de Gestión Avanzado 🍞",
                       width=90))

def mostrar_menu_principal():
    """Muestra el menú principal del sistema"""
    console.print("\n[bold cyan]=== 🏠 MENÚ PRINCIPAL ===[/bold cyan]")
    console.print("1️⃣ 📦 Gestión de Productos")
    console.print("2️⃣ 📋 Gestión de Pedidos")
    console.print("3️⃣ 📊 Reportes y Estadísticas")
    console.print("4️⃣ ⚙️ Configuración del Sistema")
    console.print("5️⃣ 💾 Respaldo de Datos")
    console.print("6️⃣ 📈 Dashboard Rápido")
    console.print("7️⃣ 👋 Salir")
    return input("\n⚡ Seleccione una opción: ")

def mostrar_dashboard_rapido(datos, config):
    """Muestra un dashboard rápido con información clave"""
    from modulos.gestion_archivos import cargar_pedidos
    
    console.print("\n[bold green]=== 📊 DASHBOARD RÁPIDO ===[/bold green]")
    
    # Estadísticas de productos
    total_productos = len(datos["productos"])
    productos_stock_bajo = [p for p in datos["productos"] if p["cantidad_en_stock"] < config["inventario"]["stock_minimo"]]
    valor_inventario = sum(p["cantidad_en_stock"] * p["precio_venta"] for p in datos["productos"])
    
    # Estadísticas de ventas
    datos_pedidos = cargar_pedidos()
    total_pedidos = len(datos_pedidos["pedidos"])
    total_ventas = sum(pedido["total"] for pedido in datos_pedidos["pedidos"])
    
    # Crear tabla de resumen
    from rich.table import Table
    tabla_resumen = Table(title="📈 Resumen del Negocio")
    tabla_resumen.add_column("Métrica", style="cyan", justify="center")
    tabla_resumen.add_column("Valor", style="green", justify="center")
    tabla_resumen.add_column("Estado", style="yellow", justify="center")
    
    tabla_resumen.add_row("Total Productos", str(total_productos), "✅")
    tabla_resumen.add_row("Productos Stock Bajo", str(len(productos_stock_bajo)), "⚠️" if productos_stock_bajo else "✅")
    tabla_resumen.add_row("Valor Inventario", f"${valor_inventario:.2f}", "💰")
    tabla_resumen.add_row("Total Pedidos", str(total_pedidos), "📋")
    tabla_resumen.add_row("Total Ventas", f"${total_ventas:.2f}", "💵")
    
    console.print(tabla_resumen)
    
    # Alertas importantes
    if productos_stock_bajo:
        console.print("\n[bold red]⚠️ ALERTAS IMPORTANTES:[/bold red]")
        for producto in productos_stock_bajo[:3]:  # Mostrar solo los primeros 3
            console.print(f"   • {producto['nombre']} - Stock: {producto['cantidad_en_stock']}")
        if len(productos_stock_bajo) > 3:
            console.print(f"   • ... y {len(productos_stock_bajo) - 3} productos más")

def crear_respaldo_manual():
    """Crea un respaldo manual de los datos"""
    from modulos.gestion_archivos import crear_respaldo
    
    console.print("\n[bold cyan]Creando respaldo manual...[/bold cyan]")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        
        task = progress.add_task("Creando respaldo...", total=100)
        progress.update(task, advance=50)
        
        if crear_respaldo():
            progress.update(task, advance=50)
            console.print("\n[bold green]✅ Respaldo creado exitosamente[/bold green]")
        else:
            console.print("\n[bold red]❌ Error al crear respaldo[/bold red]")

def main():
    """Función principal del programa"""
    # Mostrar el banner de bienvenida
    mostrar_banner()
    
    # Cargar configuración
    config = cargar_configuracion()
    
    # Mostrar información de inicio
    console.print(f"\n[bold blue]🏢 {config['sistema']['nombre_empresa']} - v{config['sistema']['version']}[/bold blue]")
    console.print(f"[dim]Zona horaria: {config['sistema']['zona_horaria']} | Idioma: {config['sistema']['idioma']}[/dim]")
    
    # Cargar datos desde el archivo JSON
    console.print("\n[dim]Cargando datos del sistema...[/dim]")
    datos = cargar_datos()
    
    # Menú principal
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            gestionar_productos(datos)
            # Guardamos los cambios después de gestionar productos
            guardar_datos(datos)
        elif opcion == "2":
            gestionar_pedidos(datos)
            # Guardamos los cambios después de gestionar pedidos
            guardar_datos(datos)
        elif opcion == "3":
            gestionar_reportes(datos)
        elif opcion == "4":
            config = gestionar_configuracion()
        elif opcion == "5":
            crear_respaldo_manual()
        elif opcion == "6":
            mostrar_dashboard_rapido(datos, config)
        elif opcion == "7":
            break
        else:
            console.print("\n[bold yellow]⚠ Opción no válida[/bold yellow]")
        
        if opcion not in ["7"]:
            input("\n⏸️ Presione Enter para continuar...")
    
    # Mensaje de despedida
    console.print("\n[bold green]¡Gracias por usar el sistema de Maison du Pain![/bold green]")
    console.print("[dim]Sistema de Gestión Avanzado v2.0.0[/dim]")

if __name__ == "__main__":
    main() 