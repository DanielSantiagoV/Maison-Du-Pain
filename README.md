# 🥖 Maison du Pain - Sistema de Gestión de Panadería

Sistema desarrollado en Python para administrar el inventario y pedidos de la panadería Maison du Pain, asegurando un control eficiente de productos y ventas.

## 🌟 Características Principales

### 📦 Gestión de Productos
- 📌 Registro completo de productos de panadería (panes, pasteles, postres, etc.).
- 📂 Almacenamiento de información detallada:
  - 🏷️ Nombre del producto
  - 🏗️ Categoría (pan, pastel, postre)
  - 📝 Descripción
  - 🏭 Proveedor
  - 📦 Cantidad en stock
  - 💰 Precios de venta y compra
- 🔢 Generación automática de códigos de producto basados en categoría (PN-001, PS-001, PT-001).
- ⚙️ Funcionalidades:
  - ➕ Agregar, ✏️ editar y ❌ eliminar productos.
  - 📋 Listado detallado de productos registrados.

### 📝 Gestión de Pedidos
- 🛍️ Creación y administración de pedidos de clientes.
- 📄 Registro detallado de productos en cada pedido:
  - 🔢 Cantidad
  - 💲 Precio por unidad
  - #️⃣ Número de línea
- 🔄 Funcionalidades completas de edición y eliminación de pedidos.
- 🧮 Cálculo automático de totales en cada compra.

### 📊 Inventario Automatizado
- 🔄 Actualización automática del stock al registrar pedidos.
- 📈 Control de inventario en tiempo real.
- ⚠️ Sistema de alertas para productos con stock bajo (menos de 5 unidades).
- 🔙 Devolución automática de stock al eliminar pedidos.

### 🔍 Consultas y Búsquedas
- 🔎 Búsqueda flexible de productos:
  - 🔤 Por nombre
  - 🏷️ Por categoría
  - 🔢 Por código
- 📑 Filtrado de pedidos:
  - #️⃣ Por código de pedido
  - 🛒 Por productos incluidos
- 📊 Visualización detallada de información.

### 💾 Manejo de Archivos y Persistencia
- 🗂️ Almacenamiento de datos en formato JSON.
- 📂 Estructura organizada de archivos:
  - `📜 datos_panaderia.json`: Información de productos.
  - `📜 pedidos.json`: Registro de pedidos.
- ♻️ Persistencia de datos entre sesiones.
- ✅ Manejo de errores y validaciones.

### 👥 Interfaz de Usuario
- 🏠 Menús intuitivos y organizados.
- ✅ Confirmaciones para acciones críticas.
- ℹ️ Mensajes informativos claros.
- 📊 Tablas formateadas para mejor visualización.
- 🎨 Uso de colores y emojis para mejor experiencia.

## 🛠️ Tecnologías Utilizadas
- 🐍 **Python 3**
- 📄 **JSON** para almacenamiento de datos.
- 🎨 **Rich** para mejorar la visualización en la terminal.

## 📋 Requisitos
- 🖥️ Python 3.6 o superior.
- 📦 Instalar dependencias con:
  ```sh
  pip install rich


## 🚀 Instalación y Uso

### Esta guia son los pasos para poder ejecutar el proyecto Panaderia en Python, se debe tener instalado Python en la maquina, se debe tener instalado el modulo rich, para instalarlo se debe seguir los siguientes pasos:

1. 
    ```pip-requirements
    rich>=13.0.0
    ```

2. **Abre una terminal o línea de comandos**.

3. **Navega al directorio donde está el archivo `requirements.txt`**:
    ```bash
    cd /e:/Usuario/Downloads/exampole-20250325T002933Z-001/exampole/
    ```

4. **Instala las dependencias usando `pip`**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Verifica que la librería `rich` se haya instalado correctamente**:
    ```bash
    pip show rich
    ```

Fuente: [rich](https://pypi.org/project/rich/)
Fin de la guia.
## Ejecutar el proyecto


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




