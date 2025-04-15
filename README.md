# 🥖 Maison du Pain - Sistema de Gestión de Panadería

Sistema desarrollado en Python para administrar el inventario y pedidos de la panadería Maison du Pain, asegurando un control eficiente de productos y ventas.

## 🚀 Características

- 📦 Gestión completa de productos de panadería
- 🛍️ Sistema de pedidos y ventas
- 📊 Control de inventario automatizado
- 🔍 Búsqueda y consultas avanzadas
- 💾 Almacenamiento seguro de datos en JSON
- 👥 Interfaz de usuario intuitiva
- 📈 Reportes y estadísticas
- 🔄 Actualización automática de stock

## 📂 Estructura del Proyecto

```
maison-du-pain/
│
├── 📁 modulos/                 # Módulos principales
│   ├── gestion_productos.py    # Gestión de productos
│   ├── gestion_pedidos.py      # Gestión de pedidos
│   └── gestion_archivos.py     # Manejo de archivos
│
├── 📁 datos/                   # Almacenamiento de datos
│   ├── datos_panaderia.json    # Datos de productos
│   └── pedidos.json            # Registro de pedidos
│
├── 📄 main.py                  # Punto de entrada principal
└── 📄 README.md                # Documentación
```

## 🛠️ Requisitos

- 🐍 Python 3.6+
- 📚 Bibliotecas:
  - 🎨 rich: Para mejorar la visualización en terminal
  - 📝 json: Para manejo de archivos JSON (incluido en Python)
  - 📅 datetime: Para manejo de fechas (incluido en Python)
  - 💻 os: Para operaciones del sistema (incluido en Python)

## 📦 Instalación

1. 📥 Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/Maison-du-Pain.git
   ```

2. 📂 Navega al directorio del proyecto:
   ```
   cd Maison-du-Pain
   ```

3. ⚙️ Instala las dependencias:
   ```
   pip install rich
   ```

## 🛠️ Requisitos y Dependencias

### Dependencias Principales
```pip-requirements
rich>=13.0.0
```

### Verificación de la Instalación
Para verificar que todo está instalado correctamente, puedes ejecutar:
```bash
python -c "import rich; print('✅ Rich instalado correctamente')"
```

## 🚀 Uso

Para iniciar el sistema, ejecuta:

```
python main.py
```

## 🗂️ Almacenamiento de Datos

Los datos se almacenan en formato JSON en los siguientes archivos:
- `datos_panaderia.json`: Información de productos
- `pedidos.json`: Registro de pedidos

## 📝 Estructura de Datos JSON

### 📦 Estructura de Productos
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

### 🛍️ Estructura de Pedidos
```json
{
  "codigo_pedido": "PED-001",
  "codigo_cliente": "CLI-001",
  "fecha_pedido": "2024-03-21 15:30:00",
  "estado": "pendiente",
  "total": 150.00,
  "detalles": [
    {
      "numero_linea": 1,
      "codigo_producto": "PAN-001",
      "cantidad": 2,
      "precio_unidad": 3.50,
      "subtotal": 7.00
    }
  ]
}
```

## 📊 Funcionalidades Principales

### 📦 Gestión de Productos
- 📝 Registro de nuevos productos
- ✏️ Modificación de productos existentes
- 🗑️ Eliminación de productos
- 👀 Visualización de inventario
- 📈 Control de stock

### 🛍️ Gestión de Pedidos
- 💸 Creación de nuevos pedidos
- 📋 Modificación de pedidos existentes
- 🗑️ Cancelación de pedidos
- 📊 Visualización de pedidos
- 💰 Cálculo automático de totales

### 📊 Inventario
- 🔄 Actualización automática de stock
- ⚠️ Alertas de stock bajo
- 📈 Control de inventario en tiempo real
- 📊 Reportes de inventario

## 🤝 Contribución

Si deseas contribuir a este proyecto, por favor:

1. 🍴 Haz un Fork del proyecto
2. 🌿 Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. ✏️ Realiza tus cambios
4. 💾 Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
5. 📤 Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
6. 🔄 Abre un Pull Request

## 👥 Roles del Equipo

### 🎯 Product Owner
- Daniel Santiago Vinasco

### 👨‍💻 Desarrollador
- Daniel Santiago Vinasco

---

Desarrollado con ❤️ para Maison du Pain

### 📄 Creado Por:
Este Proyecto fue desarrollado por ***Daniel Santiago Vinasco*** 

---

### ✅ ¿Qué incluye este README?
✔ 📋 Características detalladas del sistema de gestión de panadería  
✔ 📁 Estructura del proyecto clara y organizada  
✔ 🖥️ Código del menú principal con opciones intuitivas  
✔ 📊 Funciones clave como gestión de productos, pedidos e inventario  
✔ 💾 Estructura de los JSON con ejemplos detallados  
✔ 🚀 Instalación y uso con pasos claros  
✔ 🎨 Estética profesional con emojis y formato Markdown limpio  

---

- 🔥 **¡Github: https://github.com/DanielSantiagoV !🚀**




