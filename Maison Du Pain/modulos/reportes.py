"""
Módulo para generar reportes y estadísticas
Proporciona análisis detallado de productos, ventas y rendimiento
"""
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from datetime import datetime, timedelta
import json
import os
from collections import defaultdict, Counter

console = Console()

def mostrar_menu_reportes():
    """Muestra el menú de reportes disponibles"""
    console.print("\n[bold cyan]=== 📊 REPORTES Y ESTADÍSTICAS ===[/bold cyan]")
    console.print("1️⃣ 📈 Reporte de Ventas")
    console.print("2️⃣ 📦 Análisis de Inventario")
    console.print("3️⃣ 🏆 Productos Más Vendidos")
    console.print("4️⃣ 💰 Análisis Financiero")
    console.print("5️⃣ 📅 Reporte por Período")
    console.print("6️⃣ 📋 Exportar Reportes")
    console.print("7️⃣ 🔙 Volver al Menú Principal")
    return input("\n⚡ Seleccione una opción: ")

def generar_reporte_ventas(datos_productos):
    """Genera un reporte detallado de ventas"""
    from modulos.gestion_archivos import cargar_pedidos, cargar_detalles_pedidos
    
    datos_pedidos = cargar_pedidos()
    datos_detalles = cargar_detalles_pedidos()
    
    if not datos_pedidos["pedidos"]:
        console.print("\n[bold yellow]⚠ No hay pedidos para generar reporte[/bold yellow]")
        return
    
    # Análisis de ventas
    total_ventas = sum(pedido["total"] for pedido in datos_pedidos["pedidos"])
    total_pedidos = len(datos_pedidos["pedidos"])
    promedio_por_pedido = total_ventas / total_pedidos if total_pedidos > 0 else 0
    
    # Análisis por fecha
    ventas_por_fecha = defaultdict(float)
    for pedido in datos_pedidos["pedidos"]:
        fecha = pedido["fecha_pedido"].split()[0]  # Solo la fecha
        ventas_por_fecha[fecha] += pedido["total"]
    
    # Crear tabla de resumen
    tabla_resumen = Table(title="📊 Resumen de Ventas")
    tabla_resumen.add_column("Métrica", style="cyan", justify="center")
    tabla_resumen.add_column("Valor", style="green", justify="center")
    
    tabla_resumen.add_row("Total de Ventas", f"${total_ventas:.2f}")
    tabla_resumen.add_row("Total de Pedidos", str(total_pedidos))
    tabla_resumen.add_row("Promedio por Pedido", f"${promedio_por_pedido:.2f}")
    tabla_resumen.add_row("Días con Ventas", str(len(ventas_por_fecha)))
    
    console.print(tabla_resumen)
    
    # Tabla de ventas por fecha
    if ventas_por_fecha:
        tabla_fechas = Table(title="📅 Ventas por Fecha")
        tabla_fechas.add_column("Fecha", style="cyan", justify="center")
        tabla_fechas.add_column("Total Ventas", style="green", justify="center")
        
        for fecha, total in sorted(ventas_por_fecha.items()):
            tabla_fechas.add_row(fecha, f"${total:.2f}")
        
        console.print(tabla_fechas)

def analizar_inventario(datos):
    """Analiza el estado del inventario"""
    if not datos["productos"]:
        console.print("\n[bold yellow]⚠ No hay productos para analizar[/bold yellow]")
        return
    
    # Estadísticas generales
    total_productos = len(datos["productos"])
    total_stock = sum(p["cantidad_en_stock"] for p in datos["productos"])
    valor_inventario = sum(p["cantidad_en_stock"] * p["precio_venta"] for p in datos["productos"])
    
    # Productos con stock bajo
    productos_stock_bajo = [p for p in datos["productos"] if p["cantidad_en_stock"] < 5]
    
    # Análisis por categoría
    stock_por_categoria = defaultdict(int)
    valor_por_categoria = defaultdict(float)
    
    for producto in datos["productos"]:
        categoria = producto["categoria"]
        stock_por_categoria[categoria] += producto["cantidad_en_stock"]
        valor_por_categoria[categoria] += producto["cantidad_en_stock"] * producto["precio_venta"]
    
    # Tabla de resumen
    tabla_resumen = Table(title="📦 Análisis de Inventario")
    tabla_resumen.add_column("Métrica", style="cyan", justify="center")
    tabla_resumen.add_column("Valor", style="green", justify="center")
    
    tabla_resumen.add_row("Total de Productos", str(total_productos))
    tabla_resumen.add_row("Total en Stock", str(total_stock))
    tabla_resumen.add_row("Valor del Inventario", f"${valor_inventario:.2f}")
    tabla_resumen.add_row("Productos con Stock Bajo", str(len(productos_stock_bajo)))
    
    console.print(tabla_resumen)
    
    # Tabla por categoría
    tabla_categorias = Table(title="🏷️ Stock por Categoría")
    tabla_categorias.add_column("Categoría", style="cyan", justify="center")
    tabla_categorias.add_column("Cantidad", style="green", justify="center")
    tabla_categorias.add_column("Valor", style="yellow", justify="center")
    
    for categoria in stock_por_categoria:
        tabla_categorias.add_row(
            categoria.title(),
            str(stock_por_categoria[categoria]),
            f"${valor_por_categoria[categoria]:.2f}"
        )
    
    console.print(tabla_categorias)
    
    # Alertas de stock bajo
    if productos_stock_bajo:
        tabla_alertas = Table(title="⚠️ Productos con Stock Bajo")
        tabla_alertas.add_column("Código", style="red", justify="center")
        tabla_alertas.add_column("Nombre", style="red", justify="center")
        tabla_alertas.add_column("Stock Actual", style="red", justify="center")
        
        for producto in productos_stock_bajo:
            tabla_alertas.add_row(
                producto["codigo_producto"],
                producto["nombre"],
                str(producto["cantidad_en_stock"])
            )
        
        console.print(tabla_alertas)

def productos_mas_vendidos(datos_productos):
    """Analiza los productos más vendidos"""
    from modulos.gestion_archivos import cargar_detalles_pedidos
    
    datos_detalles = cargar_detalles_pedidos()
    
    if not datos_detalles["detalles_pedidos"]:
        console.print("\n[bold yellow]⚠ No hay ventas para analizar[/bold yellow]")
        return
    
    # Contar ventas por producto
    ventas_por_producto = defaultdict(int)
    ingresos_por_producto = defaultdict(float)
    
    for detalle_pedido in datos_detalles["detalles_pedidos"]:
        for detalle in detalle_pedido["detalles"]:
            codigo = detalle["codigo_producto"]
            cantidad = detalle["cantidad"]
            subtotal = detalle["subtotal"]
            
            ventas_por_producto[codigo] += cantidad
            ingresos_por_producto[codigo] += subtotal
    
    # Obtener nombres de productos
    nombres_productos = {}
    for producto in datos_productos["productos"]:
        nombres_productos[producto["codigo_producto"]] = producto["nombre"]
    
    # Crear tabla de productos más vendidos
    tabla_ventas = Table(title="🏆 Productos Más Vendidos")
    tabla_ventas.add_column("Posición", style="cyan", justify="center")
    tabla_ventas.add_column("Código", style="green", justify="center")
    tabla_ventas.add_column("Nombre", style="white", justify="center")
    tabla_ventas.add_column("Cantidad Vendida", style="yellow", justify="center")
    tabla_ventas.add_column("Ingresos", style="magenta", justify="center")
    
    # Ordenar por cantidad vendida
    productos_ordenados = sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True)
    
    for i, (codigo, cantidad) in enumerate(productos_ordenados[:10], 1):
        nombre = nombres_productos.get(codigo, "Producto Desconocido")
        ingresos = ingresos_por_producto[codigo]
        
        tabla_ventas.add_row(
            str(i),
            codigo,
            nombre,
            str(cantidad),
            f"${ingresos:.2f}"
        )
    
    console.print(tabla_ventas)

def analisis_financiero(datos_productos):
    """Realiza un análisis financiero del negocio"""
    from modulos.gestion_archivos import cargar_pedidos
    
    datos_pedidos = cargar_pedidos()
    
    if not datos_pedidos["pedidos"]:
        console.print("\n[bold yellow]⚠ No hay datos financieros para analizar[/bold yellow]")
        return
    
    # Cálculos financieros
    total_ventas = sum(pedido["total"] for pedido in datos_pedidos["pedidos"])
    
    # Calcular costo de productos vendidos
    costo_ventas = 0
    from modulos.gestion_archivos import cargar_detalles_pedidos
    datos_detalles = cargar_detalles_pedidos()
    
    for detalle_pedido in datos_detalles["detalles_pedidos"]:
        for detalle in detalle_pedido["detalles"]:
            codigo = detalle["codigo_producto"]
            cantidad = detalle["cantidad"]
            
            # Buscar precio de proveedor
            for producto in datos_productos["productos"]:
                if producto["codigo_producto"] == codigo:
                    costo_ventas += cantidad * producto["precio_proveedor"]
                    break
    
    # Calcular márgenes
    ganancia_bruta = total_ventas - costo_ventas
    margen_bruto = (ganancia_bruta / total_ventas * 100) if total_ventas > 0 else 0
    
    # Valor del inventario actual
    valor_inventario = sum(p["cantidad_en_stock"] * p["precio_venta"] for p in datos_productos["productos"])
    costo_inventario = sum(p["cantidad_en_stock"] * p["precio_proveedor"] for p in datos_productos["productos"])
    
    # Tabla de análisis financiero
    tabla_financiera = Table(title="💰 Análisis Financiero")
    tabla_financiera.add_column("Concepto", style="cyan", justify="center")
    tabla_financiera.add_column("Valor", style="green", justify="center")
    
    tabla_financiera.add_row("Total de Ventas", f"${total_ventas:.2f}")
    tabla_financiera.add_row("Costo de Ventas", f"${costo_ventas:.2f}")
    tabla_financiera.add_row("Ganancia Bruta", f"${ganancia_bruta:.2f}")
    tabla_financiera.add_row("Margen Bruto", f"{margen_bruto:.1f}%")
    tabla_financiera.add_row("Valor del Inventario", f"${valor_inventario:.2f}")
    tabla_financiera.add_row("Costo del Inventario", f"${costo_inventario:.2f}")
    
    console.print(tabla_financiera)

def reporte_por_periodo(datos_productos):
    """Genera reporte de ventas por período específico"""
    from modulos.gestion_archivos import cargar_pedidos, cargar_detalles_pedidos
    
    datos_pedidos = cargar_pedidos()
    
    if not datos_pedidos["pedidos"]:
        console.print("\n[bold yellow]⚠ No hay pedidos para generar reporte[/bold yellow]")
        return
    
    console.print("\n[bold cyan]Seleccione el período:[/bold cyan]")
    console.print("1️⃣ Últimos 7 días")
    console.print("2️⃣ Últimos 30 días")
    console.print("3️⃣ Este mes")
    console.print("4️⃣ Período personalizado")
    
    opcion = input("\n⚡ Seleccione una opción: ")
    
    fecha_inicio = None
    fecha_fin = datetime.now()
    
    if opcion == "1":
        fecha_inicio = fecha_fin - timedelta(days=7)
    elif opcion == "2":
        fecha_inicio = fecha_fin - timedelta(days=30)
    elif opcion == "3":
        fecha_inicio = fecha_fin.replace(day=1)
    elif opcion == "4":
        try:
            fecha_inicio_str = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
        except ValueError:
            console.print("\n[bold red]❌ Formato de fecha inválido[/bold red]")
            return
    else:
        console.print("\n[bold red]❌ Opción no válida[/bold red]")
        return
    
    # Filtrar pedidos por período
    pedidos_periodo = []
    for pedido in datos_pedidos["pedidos"]:
        fecha_pedido = datetime.strptime(pedido["fecha_pedido"], "%Y-%m-%d %H:%M:%S")
        if fecha_inicio <= fecha_pedido <= fecha_fin:
            pedidos_periodo.append(pedido)
    
    if not pedidos_periodo:
        console.print("\n[bold yellow]⚠ No hay pedidos en el período seleccionado[/bold yellow]")
        return
    
    # Análisis del período
    total_ventas = sum(pedido["total"] for pedido in pedidos_periodo)
    total_pedidos = len(pedidos_periodo)
    promedio_por_pedido = total_ventas / total_pedidos
    
    # Tabla de resumen del período
    tabla_periodo = Table(title=f"📊 Reporte del Período: {fecha_inicio.strftime('%Y-%m-%d')} a {fecha_fin.strftime('%Y-%m-%d')}")
    tabla_periodo.add_column("Métrica", style="cyan", justify="center")
    tabla_periodo.add_column("Valor", style="green", justify="center")
    
    tabla_periodo.add_row("Total de Ventas", f"${total_ventas:.2f}")
    tabla_periodo.add_row("Total de Pedidos", str(total_pedidos))
    tabla_periodo.add_row("Promedio por Pedido", f"${promedio_por_pedido:.2f}")
    
    console.print(tabla_periodo)

def exportar_reportes(datos_productos):
    """Exporta reportes a archivos JSON y CSV"""
    from modulos.gestion_archivos import cargar_pedidos, cargar_detalles_pedidos
    
    console.print("\n[bold cyan]Exportando reportes...[/bold cyan]")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        
        task = progress.add_task("Generando reportes...", total=100)
        
        # Crear directorio de reportes
        reportes_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reportes")
        os.makedirs(reportes_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Reporte de productos
        progress.update(task, advance=20)
        reporte_productos = {
            "fecha_generacion": datetime.now().isoformat(),
            "total_productos": len(datos_productos["productos"]),
            "productos": datos_productos["productos"]
        }
        
        with open(os.path.join(reportes_dir, f"productos_{timestamp}.json"), "w", encoding="utf-8") as f:
            json.dump(reporte_productos, f, indent=4, ensure_ascii=False)
        
        # Reporte de ventas
        progress.update(task, advance=20)
        datos_pedidos = cargar_pedidos()
        datos_detalles = cargar_detalles_pedidos()
        
        reporte_ventas = {
            "fecha_generacion": datetime.now().isoformat(),
            "total_pedidos": len(datos_pedidos["pedidos"]),
            "total_ventas": sum(pedido["total"] for pedido in datos_pedidos["pedidos"]),
            "pedidos": datos_pedidos["pedidos"],
            "detalles": datos_detalles["detalles_pedidos"]
        }
        
        with open(os.path.join(reportes_dir, f"ventas_{timestamp}.json"), "w", encoding="utf-8") as f:
            json.dump(reporte_ventas, f, indent=4, ensure_ascii=False)
        
        # Reporte consolidado
        progress.update(task, advance=20)
        reporte_consolidado = {
            "fecha_generacion": datetime.now().isoformat(),
            "resumen": {
                "total_productos": len(datos_productos["productos"]),
                "total_pedidos": len(datos_pedidos["pedidos"]),
                "total_ventas": sum(pedido["total"] for pedido in datos_pedidos["pedidos"]),
                "valor_inventario": sum(p["cantidad_en_stock"] * p["precio_venta"] for p in datos_productos["productos"])
            }
        }
        
        with open(os.path.join(reportes_dir, f"consolidado_{timestamp}.json"), "w", encoding="utf-8") as f:
            json.dump(reporte_consolidado, f, indent=4, ensure_ascii=False)
        
        progress.update(task, advance=40)
    
    console.print(f"\n[bold green]✅ Reportes exportados exitosamente a: {reportes_dir}[/bold green]")

def gestionar_reportes(datos_productos):
    """Función principal para gestionar reportes"""
    while True:
        opcion = mostrar_menu_reportes()
        
        if opcion == "1":
            generar_reporte_ventas(datos_productos)
        elif opcion == "2":
            analizar_inventario(datos_productos)
        elif opcion == "3":
            productos_mas_vendidos(datos_productos)
        elif opcion == "4":
            analisis_financiero(datos_productos)
        elif opcion == "5":
            reporte_por_periodo(datos_productos)
        elif opcion == "6":
            exportar_reportes(datos_productos)
        elif opcion == "7":
            break
        else:
            console.print("\n[bold yellow]⚠ Opción no válida[/bold yellow]")
        
        if opcion != "7":
            input("\n⏸️ Presione Enter para continuar...") 