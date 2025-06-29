# 📚 Documentación Técnica - Maison du Pain v2.0.0

## 🏗️ Arquitectura del Sistema

### Estructura de Módulos

```
modulos/
├── gestion_archivos.py    # Core: Manejo de archivos y respaldos
├── gestion_productos.py   # Lógica de negocio: Productos
├── gestion_pedidos.py     # Lógica de negocio: Pedidos
├── reportes.py           # Análisis y reportes
├── configuracion.py      # Gestión de configuración
└── utilidades.py         # Funciones auxiliares
```

### Flujo de Datos

1. **Inicialización**: `main.py` → `configuracion.py` → `gestion_archivos.py`
2. **Carga de Datos**: `gestion_archivos.py` → JSON files
3. **Operaciones**: Módulos específicos → `utilidades.py` (validaciones)
4. **Persistencia**: `gestion_archivos.py` → JSON files + respaldos
5. **Reportes**: `reportes.py` → Análisis de datos → Exportación

## 🔧 API de Módulos

### gestion_archivos.py

#### Funciones Principales
```python
def cargar_datos() -> dict
    """Carga datos desde JSON con validación y reparación automática"""

def guardar_datos(datos: dict) -> None
    """Guarda datos con respaldo automático"""

def crear_respaldo() -> bool
    """Crea respaldo timestamped de todos los datos"""

def validar_datos(datos: dict) -> list
    """Valida estructura y tipos de datos"""

def reparar_datos(datos: dict) -> dict
    """Repara datos corruptos automáticamente"""
```

#### Estructura de Datos
```python
DATOS_STRUCTURE = {
    "productos": [
        {
            "codigo_producto": str,      # PAN-001, PT-001, PS-001
            "nombre": str,
            "categoria": str,            # "pan", "pastel", "postre"
            "descripcion": str,
            "proveedor": str,
            "cantidad_en_stock": int,
            "precio_venta": float,
            "precio_proveedor": float
        }
    ]
}
```

### gestion_productos.py

#### Funciones Principales
```python
def gestionar_productos(datos: dict) -> None
    """Función principal del módulo"""

def agregar_producto(datos: dict) -> None
    """Agrega producto con validación"""

def listar_productos(datos: dict) -> str
    """Lista productos en tabla formateada"""

def buscar_producto(datos: dict) -> None
    """Búsqueda flexible por código o nombre"""

def editar_producto(datos: dict) -> None
    """Edición con validación de campos"""

def eliminar_producto(datos: dict) -> None
    """Eliminación con confirmación"""
```

### gestion_pedidos.py

#### Funciones Principales
```python
def gestionar_pedidos(datos_productos: dict) -> None
    """Función principal del módulo"""

def crear_pedido(datos_productos: dict) -> None
    """Crea pedido con actualización de stock"""

def listar_pedidos() -> None
    """Lista pedidos con opción de ver detalles"""

def buscar_pedido() -> None
    """Búsqueda por código de pedido o cliente"""

def editar_pedido() -> None
    """Edición con recálculo de totales"""

def eliminar_pedido() -> None
    """Eliminación con devolución de stock"""
```

### reportes.py

#### Funciones Principales
```python
def gestionar_reportes(datos_productos: dict) -> None
    """Función principal del módulo"""

def generar_reporte_ventas(datos_productos: dict) -> None
    """Análisis detallado de ventas"""

def analizar_inventario(datos: dict) -> None
    """Estado del inventario y alertas"""

def productos_mas_vendidos(datos_productos: dict) -> None
    """Ranking de productos por ventas"""

def analisis_financiero(datos_productos: dict) -> None
    """Análisis de márgenes y ganancias"""

def exportar_reportes(datos_productos: dict) -> None
    """Exportación a JSON y CSV"""
```

### configuracion.py

#### Funciones Principales
```python
def gestionar_configuracion() -> dict
    """Función principal del módulo"""

def cargar_configuracion() -> dict
    """Carga configuración con valores por defecto"""

def guardar_configuracion(config: dict) -> bool
    """Guarda configuración en JSON"""

def configurar_empresa(config: dict) -> None
    """Configuración de datos de empresa"""

def configurar_inventario(config: dict) -> None
    """Configuración de parámetros de inventario"""
```

### utilidades.py

#### Funciones Principales
```python
def validar_entrada_numerica(mensaje: str, min_val: float = None, max_val: float = None) -> float
    """Validación de entrada numérica"""

def validar_entrada_entera(mensaje: str, min_val: int = None, max_val: int = None) -> int
    """Validación de entrada entera"""

def confirmar_accion(mensaje: str = "¿Está seguro?") -> bool
    """Solicita confirmación del usuario"""

def formatear_moneda(valor: float, moneda: str = "COP") -> str
    """Formatea valor como moneda"""

def exportar_a_csv(datos: list, nombre_archivo: str, campos: list) -> bool
    """Exporta datos a CSV"""

def obtener_estadisticas_rapidas(datos_productos: dict) -> dict
    """Calcula estadísticas rápidas del negocio"""
```

## 🗄️ Estructura de Archivos

### Archivos de Datos
```
datos/
├── datos_panaderia.json           # Productos principales
└── pedidos/
    ├── pedidos.json               # Encabezados de pedidos
    └── detalles_pedidos.json      # Líneas de pedidos
```

### Archivos de Sistema
```
config/
├── config.json                    # Configuración actual
└── config_ejemplo.json           # Ejemplo de configuración

backups/
├── datos_panaderia_20241219_143022.json
└── pedidos_20241219_143022/
    ├── pedidos.json
    └── detalles_pedidos.json

logs/
└── panaderia_20241219.log        # Logs diarios

reportes/
├── productos_20241219_143022.json
├── ventas_20241219_143022.json
└── consolidado_20241219_143022.json
```

## 🔍 Validaciones y Seguridad

### Validación de Datos
- **Tipos**: Verificación de tipos de datos (int, float, str)
- **Rangos**: Validación de valores mínimos y máximos
- **Formato**: Verificación de formatos (email, teléfono, códigos)
- **Integridad**: Verificación de referencias entre entidades

### Manejo de Errores
```python
try:
    # Operación crítica
    resultado = operacion_riesgosa()
except FileNotFoundError:
    # Crear archivo si no existe
    crear_archivo_por_defecto()
except json.JSONDecodeError:
    # Reparar JSON corrupto
    datos = reparar_datos(datos)
except Exception as e:
    # Log del error y recuperación graceful
    logger.error(f"Error inesperado: {e}")
    return valor_por_defecto
```

### Logs de Auditoría
```python
# Niveles de log
logging.INFO    # Operaciones normales
logging.WARNING # Situaciones anómalas
logging.ERROR   # Errores recuperables
logging.CRITICAL # Errores críticos
```

## 🚀 Optimizaciones

### Rendimiento
- **Carga Lazy**: Datos se cargan solo cuando se necesitan
- **Caché**: Configuración se mantiene en memoria
- **Validación Selectiva**: Solo se valida lo necesario
- **Respaldo Incremental**: Solo se respaldan cambios

### Memoria
- **Streaming**: Procesamiento de archivos grandes
- **Limpieza**: Eliminación automática de datos temporales
- **Compresión**: Respaldos comprimidos para ahorrar espacio

## 🧪 Testing

### Casos de Prueba Recomendados

#### Validación de Datos
```python
def test_validar_producto():
    producto_valido = {
        "codigo_producto": "PAN-001",
        "nombre": "Pan Francés",
        "categoria": "pan",
        "cantidad_en_stock": 50,
        "precio_venta": 3.50
    }
    assert validar_producto(producto_valido) == True

def test_validar_producto_invalido():
    producto_invalido = {
        "codigo_producto": "INVALID",
        "cantidad_en_stock": -5,  # Stock negativo
        "precio_venta": "no_numero"  # Precio no numérico
    }
    assert validar_producto(producto_invalido) == False
```

#### Manejo de Errores
```python
def test_archivo_corrupto():
    # Simular archivo JSON corrupto
    with open("datos_corruptos.json", "w") as f:
        f.write("{ invalid json }")
    
    datos = cargar_datos()
    assert datos is not None
    assert "productos" in datos
```

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
# Rutas personalizadas
export MAISON_PAIN_CONFIG_PATH="/custom/config.json"
export MAISON_PAIN_DATA_PATH="/custom/data/"
export MAISON_PAIN_LOG_LEVEL="DEBUG"

# Configuración de respaldos
export MAISON_PAIN_BACKUP_RETENTION_DAYS="60"
export MAISON_PAIN_BACKUP_COMPRESS="true"
```

### Configuración de Logs
```python
# Niveles de log por módulo
LOGGING_CONFIG = {
    "gestion_archivos": "INFO",
    "gestion_productos": "DEBUG",
    "gestion_pedidos": "INFO",
    "reportes": "WARNING",
    "configuracion": "INFO"
}
```

## 📊 Métricas y Monitoreo

### Métricas Clave
- **Tiempo de respuesta**: Carga y guardado de datos
- **Uso de memoria**: Consumo de RAM por operación
- **Tamaño de archivos**: Crecimiento de datos
- **Errores**: Frecuencia y tipos de errores

### Alertas
- **Stock bajo**: Productos con stock < mínimo
- **Errores críticos**: Fallos en respaldo o validación
- **Rendimiento**: Operaciones lentas
- **Espacio**: Disco lleno o respaldos antiguos

## 🔄 Migración y Actualización

### Migración v1.0 → v2.0
```python
def migrar_v1_a_v2():
    """Migra datos de la versión 1.0 a 2.0"""
    # 1. Cargar datos antiguos
    datos_v1 = cargar_datos_v1()
    
    # 2. Convertir estructura
    datos_v2 = convertir_estructura(datos_v1)
    
    # 3. Validar y reparar
    datos_v2 = validar_y_reparar(datos_v2)
    
    # 4. Crear configuración por defecto
    config = crear_config_por_defecto()
    
    # 5. Guardar nueva estructura
    guardar_datos_v2(datos_v2)
    guardar_configuracion(config)
```

### Backup y Restore
```python
def restaurar_desde_respaldo(fecha_respaldo: str):
    """Restaura sistema desde respaldo específico"""
    # 1. Verificar respaldo existe
    if not existe_respaldo(fecha_respaldo):
        raise FileNotFoundError("Respaldo no encontrado")
    
    # 2. Crear respaldo actual antes de restaurar
    crear_respaldo_manual()
    
    # 3. Restaurar archivos
    restaurar_archivos(fecha_respaldo)
    
    # 4. Validar datos restaurados
    datos = cargar_datos()
    if not validar_datos(datos):
        raise ValueError("Datos restaurados corruptos")
```

## 🤝 Contribución al Código

### Estándares de Código
- **PEP 8**: Estilo de código Python
- **Docstrings**: Documentación de funciones
- **Type Hints**: Tipos de datos explícitos
- **Error Handling**: Manejo robusto de errores

### Estructura de Commits
```
feat: nueva funcionalidad de reportes
fix: corrección en validación de productos
docs: actualización de documentación
refactor: mejora en gestión de archivos
test: agregar tests para configuración
```

### Pull Request Checklist
- [ ] Código sigue estándares PEP 8
- [ ] Funciones tienen docstrings
- [ ] Tests pasan correctamente
- [ ] Documentación actualizada
- [ ] No hay errores de linting
- [ ] Funcionalidad probada manualmente

---

**Documentación Técnica v2.0.0** - Última actualización: 2024-12-19 