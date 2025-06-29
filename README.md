# 🥖 Maison du Pain - Sistema de Gestión de Panadería v2.0.0

<p align="center"> 
  <img src="https://media.tenor.com/fWD5SZjcqHwAAAAi/cooking-nasogg.gif" width="300"/> 
</p>

<p align="center"> 
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Rich-13.0+-green?style=for-the-badge&logo=python&logoColor=white" alt="Rich">
  <img src="https://img.shields.io/badge/Version-2.0.0-orange?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="MIT License">
</p>

<p align="center">
  <strong>Sistema avanzado de gestión para panaderías con reportes, configuración personalizable y respaldos automáticos</strong>
</p>

## 🌟 Nuevas Características v2.0.0

### 🆕 Funcionalidades Principales
- 📊 **Sistema de Reportes Avanzado**: Análisis detallado de ventas, inventario y rendimiento financiero
- ⚙️ **Configuración Personalizable**: Ajustes de empresa, inventario, ventas e interfaz
- 💾 **Respaldo Automático**: Sistema de respaldos con limpieza automática
- 📈 **Dashboard Rápido**: Vista general del negocio con alertas en tiempo real
- 🔍 **Validación Mejorada**: Verificación de datos y reparación automática
- 📋 **Exportación de Datos**: Reportes en JSON y CSV
- 📝 **Logs de Auditoría**: Registro detallado de todas las operaciones

### 🔧 Mejoras Técnicas
- 🛡️ **Manejo de Errores Robusto**: Validación y recuperación de datos corruptos
- 🎨 **Interfaz Mejorada**: Más colores, emojis y tablas detalladas
- ⚡ **Rendimiento Optimizado**: Carga y guardado más eficiente
- 🔄 **Persistencia de Datos**: Estructura de archivos mejorada
- 📱 **Compatibilidad**: Funciona en Windows, macOS y Linux

## 🚀 Características Principales

### 📦 Gestión de Productos Avanzada
- 📌 **Registro Completo**: Productos con códigos únicos por categoría
- 🏷️ **Información Detallada**: Nombre, categoría, descripción, proveedor, stock, precios
- 🔢 **Códigos Automáticos**: Generación inteligente (PAN-001, PT-001, PS-001)
- ⚙️ **Operaciones CRUD**: Agregar, editar, eliminar y buscar productos
- 📊 **Análisis de Stock**: Alertas automáticas para productos con stock bajo
- 💰 **Gestión de Precios**: Precios de venta y compra con márgenes

### 📝 Gestión de Pedidos Mejorada
- 🛍️ **Creación Inteligente**: Interfaz mejorada para crear pedidos
- 📄 **Detalles Completos**: Líneas de pedido con cantidades y precios
- 🔄 **Edición Flexible**: Modificar pedidos existentes
- 🧮 **Cálculos Automáticos**: Totales, subtotales e impuestos
- 📊 **Historial Completo**: Registro de todos los pedidos
- 🔙 **Devolución de Stock**: Actualización automática al eliminar pedidos

### 📊 Sistema de Reportes (NUEVO)
- 📈 **Reporte de Ventas**: Análisis detallado por fecha y período
- 📦 **Análisis de Inventario**: Estado del stock y valor del inventario
- 🏆 **Productos Más Vendidos**: Ranking de productos por ventas
- 💰 **Análisis Financiero**: Márgenes, ganancias y costos
- 📅 **Reportes por Período**: Filtros por días, semanas, meses
- 📋 **Exportación**: Reportes en JSON y CSV

### ⚙️ Configuración del Sistema (NUEVO)
- 🏢 **Configuración de Empresa**: Nombre, idioma, zona horaria
- 📦 **Configuración de Inventario**: Stock mínimo, alertas, respaldos
- 💰 **Configuración de Ventas**: Moneda, impuestos, descuentos
- 🎨 **Configuración de Interfaz**: Colores, emojis, confirmaciones
- 📊 **Configuración de Reportes**: Exportación automática y formatos

### 💾 Sistema de Respaldo (NUEVO)
- 🔄 **Respaldo Automático**: Antes de cada guardado
- 📅 **Limpieza Automática**: Eliminación de respaldos antiguos
- 🛡️ **Recuperación**: Restauración desde respaldos
- 📁 **Organización**: Estructura de directorios mejorada

### 🔍 Validación y Seguridad (MEJORADO)
- ✅ **Validación de Datos**: Verificación de tipos y rangos
- 🔧 **Reparación Automática**: Corrección de datos corruptos
- 📝 **Logs de Auditoría**: Registro de todas las operaciones
- 🛡️ **Manejo de Errores**: Recuperación graceful de fallos

## 🛠️ Tecnologías Utilizadas

### Core
- 🐍 **Python 3.8+**: Lenguaje principal
- 📄 **JSON**: Almacenamiento de datos
- 🎨 **Rich**: Interfaz en terminal mejorada

### Dependencias Opcionales
- 📊 **Pandas**: Exportación a CSV y análisis de datos
- 🌍 **Pytz**: Manejo de zonas horarias
- 📈 **Matplotlib**: Gráficos en reportes
- 🔐 **Cryptography**: Encriptación de datos sensibles

## 📋 Requisitos del Sistema

### Mínimos
- 🖥️ **Python 3.6+** (recomendado 3.8+)
- 💾 **100 MB** de espacio en disco
- 🧠 **512 MB** de RAM

### Recomendados
- 🖥️ **Python 3.8+**
- 💾 **500 MB** de espacio en disco
- 🧠 **1 GB** de RAM
- 💻 **Terminal con soporte de colores**

## 🚀 Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/Maison-du-Pain.git
cd Maison-du-Pain
```

### 2. Instalar Dependencias

#### Instalación Mínima (Solo funcionalidades básicas)
```bash
pip install rich
```

#### Instalación Completa (Todas las funcionalidades)
```bash
pip install -r "Maison Du Pain/Requirements/requirements.txt"
```

### 3. Verificar la Instalación
```bash
python -c "import rich; print('✅ Rich instalado correctamente')"
python -c "import pandas; print('✅ Pandas instalado correctamente')"
```

### 4. Ejecutar el Sistema
```bash
cd "Maison Du Pain"
python main.py
```

## 📂 Estructura del Proyecto v2.0.0

```
Maison-Du-Pain/
├── 📁 Maison Du Pain/
│   ├── 📄 main.py                    # Punto de entrada principal
│   ├── 📁 modulos/                   # Módulos del sistema
│   │   ├── gestion_archivos.py       # Gestión de archivos y respaldos
│   │   ├── gestion_productos.py      # Gestión de productos
│   │   ├── gestion_pedidos.py        # Gestión de pedidos
│   │   ├── reportes.py              # Sistema de reportes (NUEVO)
│   │   ├── configuracion.py         # Configuración del sistema (NUEVO)
│   │   └── utilidades.py            # Funciones auxiliares (NUEVO)
│   ├── 📁 datos/                     # Almacenamiento de datos
│   │   ├── datos_panaderia.json      # Datos de productos
│   │   └── pedidos/                  # Datos de pedidos
│   │       ├── pedidos.json
│   │       └── detalles_pedidos.json
│   ├── 📁 config/                    # Configuración (NUEVO)
│   │   └── config.json
│   ├── 📁 backups/                   # Respaldos automáticos (NUEVO)
│   ├── 📁 logs/                      # Logs de auditoría (NUEVO)
│   ├── 📁 reportes/                  # Reportes exportados (NUEVO)
│   └── 📁 Requirements/
│       └── requirements.txt
└── 📄 README.md
```

## 🎯 Uso del Sistema

### Menú Principal
```
🏠 MENÚ PRINCIPAL
1️⃣ 📦 Gestión de Productos
2️⃣ 📋 Gestión de Pedidos
3️⃣ 📊 Reportes y Estadísticas
4️⃣ ⚙️ Configuración del Sistema
5️⃣ 💾 Respaldo de Datos
6️⃣ 📈 Dashboard Rápido
7️⃣ 👋 Salir
```

### Dashboard Rápido
Vista general del negocio con:
- 📊 Estadísticas de productos y ventas
- ⚠️ Alertas de stock bajo
- 💰 Valor del inventario
- 📈 Métricas clave

### Sistema de Reportes
- 📈 **Reporte de Ventas**: Análisis por fecha y período
- 📦 **Análisis de Inventario**: Estado del stock
- 🏆 **Productos Más Vendidos**: Ranking de ventas
- 💰 **Análisis Financiero**: Márgenes y ganancias
- 📅 **Reportes por Período**: Filtros personalizables
- 📋 **Exportación**: Formatos JSON y CSV

### Configuración
- 🏢 **Empresa**: Nombre, idioma, zona horaria
- 📦 **Inventario**: Stock mínimo, alertas, respaldos
- 💰 **Ventas**: Moneda, impuestos, descuentos
- 🎨 **Interfaz**: Colores, emojis, confirmaciones

## 📊 Estructura de Datos

### Productos
```json
{
  "codigo_producto": "PAN-001",
  "nombre": "Pan Francés",
  "categoria": "pan",
  "descripcion": "Pan tradicional francés",
  "proveedor": "Panadería Local",
  "cantidad_en_stock": 50,
  "precio_venta": 3.50,
  "precio_proveedor": 2.00
}
```

### Pedidos
```json
{
  "codigo_pedido": "PED-001",
  "codigo_cliente": "CL-001",
  "fecha_pedido": "2024-03-20 10:30:00",
  "estado": "pendiente",
  "total": 25.50,
  "detalles": [
    {
      "numero_linea": 1,
      "codigo_producto": "PAN-001",
      "cantidad": 3,
      "precio_unidad": 3.50,
      "subtotal": 10.50
    }
  ]
}
```

### Configuración
```json
{
  "sistema": {
    "nombre_empresa": "Maison du Pain",
    "version": "2.0.0",
    "idioma": "es",
    "zona_horaria": "America/Bogota"
  },
  "inventario": {
    "stock_minimo": 5,
    "alertas_automaticas": true,
    "respaldo_automatico": true
  }
}
```

## 🔧 Configuración Avanzada

### Variables de Entorno (Opcional)
```bash
export MAISON_PAIN_CONFIG_PATH="/ruta/personalizada/config.json"
export MAISON_PAIN_DATA_PATH="/ruta/personalizada/datos/"
export MAISON_PAIN_LOG_LEVEL="INFO"
```

### Personalización de Colores
El sistema utiliza la librería Rich para colores. Puedes personalizar:
- Colores de tablas
- Estilos de texto
- Temas de interfaz

## 📈 Reportes Disponibles

### 1. Reporte de Ventas
- Total de ventas por período
- Promedio por pedido
- Análisis por fecha
- Tendencias de ventas

### 2. Análisis de Inventario
- Estado del stock
- Productos con stock bajo
- Valor del inventario
- Análisis por categoría

### 3. Productos Más Vendidos
- Ranking de productos
- Cantidades vendidas
- Ingresos por producto
- Análisis de popularidad

### 4. Análisis Financiero
- Margen de ganancia
- Costo de ventas
- Valor del inventario
- Rentabilidad

## 🛡️ Seguridad y Respaldo

### Sistema de Respaldo
- **Automático**: Antes de cada guardado
- **Manual**: Desde el menú principal
- **Programado**: Limpieza automática de respaldos antiguos
- **Recuperación**: Restauración desde respaldos

### Validación de Datos
- Verificación de tipos de datos
- Validación de rangos
- Reparación automática de datos corruptos
- Logs de auditoría

## 🔍 Solución de Problemas

### Problemas Comunes

#### Error: "ModuleNotFoundError: No module named 'rich'"
```bash
pip install rich
```

#### Error: "Permission denied" al guardar
- Verificar permisos de escritura en el directorio
- Ejecutar como administrador si es necesario

#### Datos corruptos
- El sistema intentará reparar automáticamente
- Usar respaldos si es necesario
- Verificar logs para más detalles

### Logs de Sistema
Los logs se guardan en `logs/panaderia_YYYYMMDD.log` con:
- Operaciones realizadas
- Errores encontrados
- Respaldos creados
- Configuraciones cambiadas

## 🤝 Contribuciones

### Cómo Contribuir
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Estándares de Código
- Usar docstrings para todas las funciones
- Seguir PEP 8 para estilo de código
- Incluir tests para nuevas funcionalidades
- Documentar cambios en el README

## 📝 Changelog

### v2.0.0 (2024-12-19)
- ✨ **NUEVO**: Sistema de reportes avanzado
- ✨ **NUEVO**: Configuración personalizable
- ✨ **NUEVO**: Sistema de respaldo automático
- ✨ **NUEVO**: Dashboard rápido
- ✨ **NUEVO**: Validación mejorada de datos
- ✨ **NUEVO**: Logs de auditoría
- ✨ **NUEVO**: Exportación de datos
- 🔧 **MEJORADO**: Interfaz de usuario
- 🔧 **MEJORADO**: Manejo de errores
- 🔧 **MEJORADO**: Estructura de archivos
- 🐛 **CORREGIDO**: Varios bugs menores

### v1.0.0 (2024-03-20)
- 🎉 Lanzamiento inicial
- 📦 Gestión básica de productos
- 📋 Gestión básica de pedidos
- 💾 Almacenamiento en JSON

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Maison du Pain Development Team**
- 📧 Email: contacto@maisondepain.com
- 🌐 Website: https://maisondepain.com
- 📱 Twitter: @MaisonDuPain

## 🙏 Agradecimientos

- [Rich](https://github.com/Textualize/rich) - Por la excelente librería de interfaz en terminal
- [Python](https://python.org) - Por ser un lenguaje tan versátil
- Comunidad de desarrolladores - Por el feedback y sugerencias

## 📞 Soporte

- 🐛 **Reportar Bugs**: [Issues](https://github.com/tu-usuario/Maison-du-Pain/issues)
- 💡 **Sugerencias**: [Discussions](https://github.com/tu-usuario/Maison-du-Pain/discussions)
- 📧 **Contacto**: contacto@maisondepain.com

---

<p align="center">
  <strong>¡Gracias por usar Maison du Pain! 🥖</strong>
</p>

<p align="center">
  <em>Sistema de Gestión Avanzado v2.0.0</em>
</p>




