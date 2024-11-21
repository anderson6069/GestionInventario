# Sistema de Gestión de Inventario

Este sistema está diseñado para gestionar el inventario de productos, registrar categorías, proveedores, bodegas y controlar el stock de los productos. Permite realizar consultas detalladas sobre el estado del inventario y generar informes relacionados.

## Descripción

El Sistema de Gestión de Inventarios permite realizar las siguientes acciones:

1. **Registrar Entidades**: Productos, categorías, proveedores y bodegas.
2. **Gestión de Stock**: Agregar y retirar productos de stock, calcular el valor total de los productos en inventario.
3. **Relaciones entre Entidades**: Administrar las relaciones entre productos, categorías, proveedores y bodegas.
4. **Consultas y Reportes**: Consultar información de productos, categorías, proveedores y bodegas, así como generar informes detallados de stock.

Este sistema está desarrollado en Python utilizando la librería `tkinter` para la interfaz gráfica y sigue principios de diseño modular y estructurado.


### Requisitos del Sistema

- **Python 3.6 o superior**: Necesitas tener Python instalado en tu máquina. Si no lo tienes, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- **Tkinter**: La librería Tkinter se usa para crear la interfaz gráfica del usuario (GUI) y debe estar incluida por defecto con Python.

### Instalación de Dependencias

1. **Clonar el repositorio**

   Primero, clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/anderson6069/GestionInventario.git
   cd GestionInventario

2. **Crear un entorno virtual**

Para evitar conflictos con otras dependencias, es recomendable crear un entorno virtual. Esto garantizará que todas las dependencias del proyecto se instalen en un espacio aislado.

En Windows:

bash
Copy code
python -m venv venv

3 **Activar el entorno virtual**

En Windows:

bash
Copy code
.\venv\Scripts\activate
En macOS/Linux:

bash
Copy code
source venv/bin/activate

4. **Instalar las dependencias**

nstala todas las dependencias necesarias utilizando el archivo requirements.txt:

bash
Copy code
pip install -r requirements.txt

5. **Ejecutar el proyecto**

Para iniciar el sistema de gestión de inventarios, ejecuta el archivo main.py:

bash
Copy code
python main.py
Esto abrirá la interfaz gráfica del sistema donde podrás interactuar con todas las funcionalidades.

## Funcionalidades

1. **Registro de Entidades**
El sistema permite registrar y gestionar las siguientes entidades:

Producto
Un producto tiene los siguientes atributos:

Nombre: El nombre del producto.
Descripción: Una breve descripción del producto.
Precio: El precio de venta del producto.
Stock Inicial: La cantidad inicial del producto disponible en inventario.
Categoría: La categoría a la que pertenece el producto.
Categoría
Una categoría tiene los siguientes atributos:

Nombre: El nombre de la categoría.
Descripción: Una breve descripción de la categoría.
Proveedor
Un proveedor tiene los siguientes atributos:

Nombre: El nombre del proveedor.
Dirección: La dirección del proveedor.
Teléfono: El número de teléfono del proveedor.
Productos suministrados: Una lista de productos que el proveedor suministra.
Bodega
Una bodega tiene los siguientes atributos:

Nombre: El nombre de la bodega.
Ubicación: La ubicación física de la bodega.
Capacidad máxima: La capacidad máxima de almacenamiento de la bodega.
Productos almacenados: Una lista de productos almacenados en la bodega.
2. Gestión de Stock
Agregar Stock
El sistema permite agregar una cantidad determinada de stock a un producto existente.

Retirar Stock
El sistema permite retirar una cantidad de stock de un producto existente, reduciendo su cantidad disponible.

Calcular Valor Total del Stock
El sistema permite calcular el valor total del stock, multiplicando el precio de cada producto por la cantidad disponible.

3. Relaciones entre Entidades
El sistema gestiona las siguientes relaciones entre entidades:

Producto y Categoría:

Se puede agregar un producto a una categoría existente.
También se puede eliminar un producto de una categoría existente.
Producto y Proveedor:

Se puede agregar un producto a la lista de productos suministrados por un proveedor existente.
También se puede eliminar un producto de la lista de productos suministrados por un proveedor.
Producto y Bodega:

Un producto puede ser agregado a una bodega existente, verificando si hay espacio disponible.
También se puede retirar un producto de una bodega, asegurando que la cantidad retirada no exceda el stock disponible.
El sistema permite consultar la disponibilidad de un producto en una bodega específica.
4. Consultas y Reportes
El sistema permite realizar las siguientes consultas:

Consultar Producto
Muestra información detallada sobre un producto: nombre, descripción, precio, stock disponible, categoría y proveedor.
Consultar Categoría
Muestra información sobre una categoría: nombre, descripción y productos asociados.
Consultar Proveedor
Muestra información sobre un proveedor: nombre, dirección, teléfono y productos suministrados.
Consultar Bodega
Muestra información sobre una bodega: nombre, ubicación, capacidad máxima y productos almacenados.
Generar Informes de Stock
El sistema permite generar los siguientes informes:

Stock Total: Muestra el total del stock disponible en el sistema.
Stock por Categoría: Muestra el stock disponible por cada categoría de productos.
Stock por Proveedor: Muestra el stock disponible por cada proveedor.
Stock por Bodega: Muestra el stock disponible por cada bodega.

## Estructura del Proyecto

La estructura de archivos del proyecto es la siguiente:

GestionInventario/
├── app/
│   ├── producto.py       # Contiene la clase Producto
│   ├── categoria.py      # Contiene la clase Categoria
│   ├── proveedor.py      # Contiene la clase Proveedor
│   ├── bodega.py         # Contiene la clase Bodega
├── main.py               # Archivo principal que ejecuta el sistema
├── requirements.txt      # Lista de dependencias necesarias
├── venv/                 # Entorno virtual para gestionar dependencias
  ├── test/               # Pruebas unitarias
    │   ├── __init__.py
    │   ├── test_producto.py
    │   ├── test_categoria.py
    │   ├── test_proveedor.py
    │   └── test_bodega.py
├── .gitignore            # Archivos y directorios a ignorar por Git
├── docs/
│    ├── requerimientos.md
│    ├── UML.pdf
└── README.md             # Este archivo

## Licencia

Este proyecto está bajo la licencia MIT.

El desarrollo y la documentación de este proyecto fueron realizados por Anderson David Angulo.

Para más detalles, consulta el archivo LICENSE.
