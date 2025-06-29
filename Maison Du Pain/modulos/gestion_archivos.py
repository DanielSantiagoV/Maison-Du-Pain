"""
Módulo para la gestión de archivos JSON
Maneja la carga y guardado de datos
"""
import json
import os
import shutil
from datetime import datetime
import logging

# Obtener la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS_DIR = os.path.join(BASE_DIR, "datos")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Configurar logging
def setup_logging():
    """Configura el sistema de logging"""
    os.makedirs(LOGS_DIR, exist_ok=True)
    log_file = os.path.join(LOGS_DIR, f"panaderia_{datetime.now().strftime('%Y%m%d')}.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

def crear_respaldo():
    """Crea un respaldo automático de los datos"""
    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Respaldar archivo principal
        if os.path.exists(os.path.join(DATOS_DIR, "datos_panaderia.json")):
            backup_file = os.path.join(BACKUP_DIR, f"datos_panaderia_{timestamp}.json")
            shutil.copy2(os.path.join(DATOS_DIR, "datos_panaderia.json"), backup_file)
        
        # Respaldar pedidos
        pedidos_dir = os.path.join(DATOS_DIR, "pedidos")
        if os.path.exists(pedidos_dir):
            backup_pedidos_dir = os.path.join(BACKUP_DIR, f"pedidos_{timestamp}")
            shutil.copytree(pedidos_dir, backup_pedidos_dir)
        
        logger.info(f"Respaldo creado exitosamente: {timestamp}")
        return True
    except Exception as e:
        logger.error(f"Error al crear respaldo: {e}")
        return False

def limpiar_respaldos_antiguos(dias_retener=30):
    """Limpia respaldos más antiguos que el número de días especificado"""
    try:
        if not os.path.exists(BACKUP_DIR):
            return
        
        fecha_limite = datetime.now().timestamp() - (dias_retener * 24 * 3600)
        
        for archivo in os.listdir(BACKUP_DIR):
            ruta_archivo = os.path.join(BACKUP_DIR, archivo)
            if os.path.getctime(ruta_archivo) < fecha_limite:
                if os.path.isfile(ruta_archivo):
                    os.remove(ruta_archivo)
                elif os.path.isdir(ruta_archivo):
                    shutil.rmtree(ruta_archivo)
                logger.info(f"Respaldo eliminado: {archivo}")
    except Exception as e:
        logger.error(f"Error al limpiar respaldos: {e}")

def validar_datos(datos):
    """Valida la estructura y contenido de los datos"""
    errores = []
    
    if not isinstance(datos, dict):
        errores.append("Los datos deben ser un diccionario")
        return errores
    
    if "productos" not in datos:
        errores.append("Falta la clave 'productos' en los datos")
    else:
        for i, producto in enumerate(datos["productos"]):
            campos_requeridos = ["codigo_producto", "nombre", "categoria", "descripcion", 
                               "proveedor", "cantidad_en_stock", "precio_venta", "precio_proveedor"]
            
            for campo in campos_requeridos:
                if campo not in producto:
                    errores.append(f"Producto {i+1}: Falta el campo '{campo}'")
            
            # Validar tipos de datos
            if "cantidad_en_stock" in producto and not isinstance(producto["cantidad_en_stock"], int):
                errores.append(f"Producto {i+1}: cantidad_en_stock debe ser un número entero")
            
            if "precio_venta" in producto and not isinstance(producto["precio_venta"], (int, float)):
                errores.append(f"Producto {i+1}: precio_venta debe ser un número")
    
    return errores

def cargar_datos():
    """Carga los datos desde el archivo JSON"""
    try:
        ruta_archivo = os.path.join(DATOS_DIR, "datos_panaderia.json")
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            
        # Validar datos
        errores = validar_datos(datos)
        if errores:
            logger.warning(f"Errores de validación encontrados: {errores}")
            # Intentar reparar datos corruptos
            datos = reparar_datos(datos)
        
        logger.info("Datos cargados exitosamente")
        return datos
    except FileNotFoundError:
        logger.info("Archivo de datos no encontrado, creando estructura inicial")
        return crear_estructura_inicial()
    except json.JSONDecodeError as e:
        logger.error(f"Error al decodificar JSON: {e}")
        return crear_estructura_inicial()
    except Exception as e:
        logger.error(f"Error inesperado al cargar datos: {e}")
        return crear_estructura_inicial()

def reparar_datos(datos):
    """Intenta reparar datos corruptos o incompletos"""
    try:
        if not isinstance(datos, dict):
            datos = {}
        
        if "productos" not in datos:
            datos["productos"] = []
        
        # Reparar productos individuales
        productos_reparados = []
        for producto in datos["productos"]:
            if isinstance(producto, dict):
                producto_reparado = {
                    "codigo_producto": producto.get("codigo_producto", "DESCONOCIDO"),
                    "nombre": producto.get("nombre", "Producto sin nombre"),
                    "categoria": producto.get("categoria", "otro"),
                    "descripcion": producto.get("descripcion", "Sin descripción"),
                    "proveedor": producto.get("proveedor", "Sin proveedor"),
                    "cantidad_en_stock": int(producto.get("cantidad_en_stock", 0)),
                    "precio_venta": float(producto.get("precio_venta", 0.0)),
                    "precio_proveedor": float(producto.get("precio_proveedor", 0.0))
                }
                productos_reparados.append(producto_reparado)
        
        datos["productos"] = productos_reparados
        logger.info("Datos reparados exitosamente")
        return datos
    except Exception as e:
        logger.error(f"Error al reparar datos: {e}")
        return crear_estructura_inicial()

def guardar_datos(datos):
    """Guarda los datos en el archivo JSON"""
    try:
        # Crear respaldo antes de guardar
        crear_respaldo()
        
        # Aseguramos que existe el directorio
        os.makedirs(DATOS_DIR, exist_ok=True)
        
        ruta_archivo = os.path.join(DATOS_DIR, "datos_panaderia.json")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
        # Limpiar respaldos antiguos
        limpiar_respaldos_antiguos()
        
        logger.info("Datos guardados exitosamente")
    except Exception as e:
        logger.error(f"Error al guardar datos: {e}")
        raise

def crear_estructura_inicial():
    """Crea la estructura inicial de datos"""
    datos = {
        "productos": [
            {
                "codigo_producto": "PAN-001",
                "nombre": "Pan Francés",
                "categoria": "pan",
                "descripcion": "Pan tradicional francés crujiente",
                "proveedor": "Panadería Central",
                "cantidad_en_stock": 50,
                "precio_venta": 1.50,
                "precio_proveedor": 0.75
            },
            {
                "codigo_producto": "PASTEL-001",
                "nombre": "Torta de Chocolate",
                "categoria": "pastel",
                "descripcion": "Deliciosa torta de chocolate con cobertura",
                "proveedor": "Dulces Delicias",
                "cantidad_en_stock": 10,
                "precio_venta": 25.00,
                "precio_proveedor": 15.00
            }
        ],
        "pedidos": []
    }
    guardar_datos(datos)
    return datos

def cargar_pedidos():
    """Carga los pedidos desde el archivo JSON"""
    try:
        ruta_pedidos = os.path.join(DATOS_DIR, "pedidos")
        os.makedirs(ruta_pedidos, exist_ok=True)
        
        ruta_archivo = os.path.join(ruta_pedidos, "pedidos.json")
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        datos = {"pedidos": []}
        guardar_pedidos(datos)
        return datos

def cargar_detalles_pedidos():
    """Carga los detalles de pedidos desde el archivo JSON"""
    try:
        ruta_pedidos = os.path.join(DATOS_DIR, "pedidos")
        os.makedirs(ruta_pedidos, exist_ok=True)
        
        ruta_archivo = os.path.join(ruta_pedidos, "detalles_pedidos.json")
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        datos = {"detalles_pedidos": []}
        guardar_detalles_pedidos(datos)
        return datos

def guardar_pedidos(datos):
    """Guarda los pedidos en el archivo JSON"""
    ruta_pedidos = os.path.join(DATOS_DIR, "pedidos")
    os.makedirs(ruta_pedidos, exist_ok=True)
    
    ruta_archivo = os.path.join(ruta_pedidos, "pedidos.json")
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def guardar_detalles_pedidos(datos):
    """Guarda los detalles de pedidos en el archivo JSON"""
    ruta_pedidos = os.path.join(DATOS_DIR, "pedidos")
    os.makedirs(ruta_pedidos, exist_ok=True)
    
    ruta_archivo = os.path.join(ruta_pedidos, "detalles_pedidos.json")
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False) 