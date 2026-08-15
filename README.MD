# 🍽️ restaurante_app - Semana 9

## Programación Orientada a Objetos

### Información del estudiante

**Estudiante:** Clide Alvarado 

**Asignatura:** Programación Orientada a Objetos

**Actividad:** Tarea Semana 9 - Estructuras de datos aplicadas al proyecto restaurante_app

---

## 📌 Descripción del proyecto

`restaurante_app` es un sistema desarrollado en Python para administrar información básica de un restaurante mediante una aplicación de consola.

El proyecto permite registrar, consultar, actualizar, eliminar y listar productos, además de registrar y listar usuarios.

Esta versión corresponde a la **Semana 9** y representa una evolución del proyecto desarrollado durante las semanas anteriores.

En esta actividad se incorporan las principales estructuras de datos de Python:

* `list`
* `tuple`
* `dict`
* `set`

Cada estructura tiene una función concreta dentro del sistema y se utiliza para resolver una necesidad específica del programa.

---

## 🎯 Objetivo

Aplicar estructuras de datos de Python dentro de un proyecto desarrollado con Programación Orientada a Objetos, manteniendo una arquitectura modular y una correcta separación de responsabilidades entre:

* Modelos
* Servicios
* Interacción con el usuario

---

# 📂 Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   ├── cliente.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

---

# 🧩 Responsabilidad de cada componente

## 📦 modelos/producto.py

Contiene la clase `Producto`.

Representa la información propia de un producto del restaurante.

Sus principales atributos son:

* Código
* Nombre
* Categoría
* Precio

La clase utiliza encapsulamiento mediante atributos privados y propiedades.

---

## 👤 modelos/usuario.py

Contiene la clase `Usuario`.

Representa de forma general a una persona registrada en el sistema.

Sus principales atributos son:

* Identificación
* Nombre
* Correo electrónico

La clase se mantiene general para permitir futuras ampliaciones del sistema.

---

## 🏪 servicios/restaurante.py

Contiene la clase `Restaurante`.

Es el servicio encargado de administrar las colecciones y las operaciones principales del sistema.

Sus responsabilidades son:

* Registrar productos.
* Buscar productos.
* Actualizar productos.
* Eliminar productos.
* Listar productos.
* Registrar usuarios.
* Listar usuarios.
* Validar códigos de productos duplicados.
* Validar identificaciones de usuarios duplicadas.
* Obtener categorías únicas.

La administración de las colecciones se mantiene dentro de esta clase.

---

## 🖥️ main.py

Es el punto de entrada del programa.

Sus responsabilidades son:

* Mostrar el menú principal.
* Solicitar información mediante `input()`.
* Crear objetos `Producto` y `Usuario`.
* Utilizar los métodos de la clase `Restaurante`.
* Mostrar los resultados al usuario.
* Controlar entradas incorrectas.
* Coordinar las diferentes opciones del menú.

`main.py` no modifica directamente las listas internas de `Restaurante`.

---

## 📄 README.md

Este archivo contiene la documentación del proyecto.

Incluye:

* Descripción del sistema.
* Objetivo.
* Estructura del proyecto.
* Responsabilidad de los componentes.
* Uso de las estructuras de datos.
* Funcionalidades.
* Validaciones.
* Instrucciones para ejecutar el programa.
* Reflexión final.

---

# 🧮 Estructuras de datos utilizadas

## 1. Lista — `list`

Las listas se utilizan para administrar las colecciones dinámicas de productos y usuarios.

En la clase `Restaurante` se utilizan:

```python
self.__productos: list[Producto] = []
self.__usuarios: list[Usuario] = []
```

### Lista de productos

La lista de productos permite realizar las siguientes operaciones:

* Registrar producto.
* Buscar producto.
* Actualizar producto.
* Eliminar producto.
* Listar productos.

### Lista de usuarios

La lista de usuarios permite:

* Registrar usuarios.
* Listar usuarios.

La utilización de listas es adecuada porque la cantidad de productos y usuarios puede aumentar o disminuir durante la ejecución del programa.

---

# 2. Tupla — `tuple`

La tupla se utiliza para almacenar las opciones principales del menú.

En `main.py`:

```python
OPCIONES_MENU: tuple[str, ...] = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Salir"
)
```

La tupla es apropiada porque las opciones principales del menú se mantienen estables durante la ejecución del programa.

A diferencia de una lista, una tupla no está diseñada para modificar sus elementos después de su creación.

---

# 3. Diccionario — `dict`

El diccionario se utiliza para relacionar las opciones del menú con las funciones que deben ejecutarse.

En `main.py` se utiliza:

```python
acciones: dict[
    str,
    Callable[[], None]
] = {
    "1": lambda: registrar_producto(restaurante),
    "2": lambda: buscar_producto(restaurante),
    "3": lambda: actualizar_producto(restaurante),
    "4": lambda: eliminar_producto(restaurante),
    "5": lambda: listar_productos(restaurante),
    "6": lambda: registrar_usuario(restaurante),
    "7": lambda: listar_usuarios(restaurante),
    "8": lambda: mostrar_categorias(restaurante),
}
```

La relación utilizada es:

```text
clave → función
```

Por ejemplo:

```text
"1" → registrar_producto
"2" → buscar_producto
"3" → actualizar_producto
"4" → eliminar_producto
```

Esto permite organizar las opciones del menú y evitar una cadena extensa de condiciones `if` y `elif`.

---

# 4. Conjunto — `set`

El conjunto se utiliza para obtener las categorías únicas de los productos registrados.

En `Restaurante`:

```python
return {
    producto.categoria
    for producto in self.__productos
}
```

Los conjuntos permiten evitar elementos duplicados.

Por ejemplo, si existen productos con las siguientes categorías:

```text
Comida
Comida
Bebida
Bebida
Postre
```

el conjunto permite obtener:

```text
Comida
Bebida
Postre
```

De esta manera, el sistema puede mostrar las categorías disponibles sin repetirlas.

---

# ⚙️ Funcionalidades del sistema

El programa dispone de un menú interactivo con las siguientes opciones:

```text
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
----------------------------------------
6. Registrar usuario
7. Listar usuarios
----------------------------------------
8. Mostrar categorías
9. Salir
```

---

## 🛒 Gestión de productos

El sistema permite:

### Registrar producto

Solicita:

* Código
* Nombre
* Categoría
* Precio

El sistema verifica que el código no esté registrado anteriormente.

### Buscar producto

Permite buscar un producto mediante su código.

### Actualizar producto

Permite modificar:

* Nombre
* Categoría
* Precio

El código del producto se mantiene como identificador.

### Eliminar producto

Permite eliminar un producto mediante su código.

Antes de eliminarlo, el programa solicita confirmación.

### Listar productos

Muestra todos los productos registrados y su información.

---

# 👥 Gestión de usuarios

El sistema permite registrar usuarios utilizando:

* Identificación
* Nombre
* Correo electrónico

Antes de registrar un usuario, se comprueba que su identificación no esté duplicada.

También existe una opción para listar todos los usuarios registrados.

---

# 🏷️ Categorías únicas

La opción **8. Mostrar categorías** utiliza un conjunto (`set`) para presentar las categorías existentes sin elementos repetidos.

Ejemplo:

```text
Categorías disponibles:
- Bebida
- Comida
- Postre

Total de categorías únicas: 3
```

---

# 🛡️ Validaciones

El sistema incluye diferentes validaciones para evitar errores durante la ejecución.

### Campos vacíos

No se permite dejar campos de texto vacíos.

### Precio

El precio debe ser un valor numérico mayor que cero.

### Códigos duplicados

No se permite registrar dos productos con el mismo código.

### Identificaciones duplicadas

No se permite registrar dos usuarios con la misma identificación.

### Opciones incorrectas

Si el usuario introduce una opción que no existe en el menú, el programa muestra un mensaje de error y continúa funcionando.

### Manejo de excepciones

Se utiliza `try` y `except` para controlar errores de entrada y evitar que el programa se cierre inesperadamente.

---

# 🔄 Flujo del sistema

El funcionamiento general del programa sigue el siguiente flujo:

```text
Usuario selecciona una opción
            ↓
        main.py
            ↓
Solicita los datos mediante input()
            ↓
Crea los objetos necesarios
            ↓
Utiliza Restaurante
            ↓
Restaurante procesa la operación
            ↓
Consulta o modifica las colecciones
            ↓
main.py muestra el resultado
```

---

# 🏗️ Separación de responsabilidades

El proyecto mantiene una arquitectura modular.

```text
MODELOS
│
├── Producto
└── Usuario

       ↓

SERVICIOS
│
└── Restaurante

       ↓

INTERACCIÓN
│
└── main.py
```

### Modelos

Representan las entidades del sistema.

### Servicios

Contienen la lógica encargada de administrar las colecciones y operaciones.

### main.py

Se encarga de la interacción con el usuario y de coordinar las operaciones.

Esta separación permite mantener el código organizado y facilita futuras modificaciones.

---

# ▶️ Instalación y ejecución

## Requisitos

Se requiere:

* Python 3.10 o superior.
* Visual Studio Code recomendado.
* Terminal de comandos.

No se necesitan librerías externas.

---

## Ejecutar el programa

Primero ingresar a la carpeta del proyecto:

```bash
cd restaurante_app
```

Después ejecutar:

```bash
python main.py
```

En Windows también puede utilizarse:

```bash
py main.py
```

---

# 🧪 Ejemplo de prueba

## Registrar un producto

Seleccionar:

```text
1
```

Ingresar:

```text
Código: P001
Nombre: Hamburguesa
Categoría: Comida
Precio: 5.50
```

Resultado:

```text
Producto registrado correctamente.
```

---

## Registrar otro producto

```text
Código: P002
Nombre: Coca Cola
Categoría: Bebida
Precio: 1.50
```

---

## Registrar un producto con la misma categoría

```text
Código: P003
Nombre: Pizza
Categoría: Comida
Precio: 7.00
```

Al seleccionar la opción:

```text
8. Mostrar categorías
```

el sistema mostrará:

```text
Categorías disponibles:
- Bebida
- Comida
```

Aunque existen dos productos de la categoría `Comida`, esta aparece una sola vez gracias al uso de `set`.

---

# 📊 Resumen de las estructuras

| Estructura | Uso en el proyecto   | Finalidad                         |
| ---------- | -------------------- | --------------------------------- |
| `list`     | Productos y usuarios | Administrar colecciones dinámicas |
| `tuple`    | Opciones del menú    | Mantener información estable      |
| `dict`     | Acciones del menú    | Relacionar claves con funciones   |
| `set`      | Categorías           | Obtener valores únicos            |

---

# 💡 Importancia de seleccionar una estructura adecuada

La selección correcta de una estructura de datos permite resolver los problemas de un programa de una manera más organizada y eficiente.

Las **listas** son apropiadas para almacenar colecciones dinámicas de objetos, como los productos y usuarios del restaurante.

Las **tuplas** son útiles cuando se necesita almacenar información que no debe modificarse durante la ejecución, como las opciones principales del menú.

Los **diccionarios** permiten establecer relaciones entre claves y valores. En este proyecto se utilizan para relacionar las opciones del menú con las funciones correspondientes.

Los **conjuntos** son útiles cuando se necesita trabajar con elementos únicos. En el proyecto permiten obtener las categorías de productos sin repetirlas.

Por esta razón, no existe una única estructura de datos adecuada para todos los problemas. La estructura debe seleccionarse de acuerdo con la necesidad específica que se desea resolver.

---

# 📝 Reflexión

Durante el desarrollo de la Semana 9 se pudo comprobar la importancia de utilizar estructuras de datos dentro de un proyecto de Programación Orientada a Objetos.

La incorporación de listas permitió administrar de manera organizada los productos y usuarios. La tupla permitió mantener las opciones principales del menú de forma estable. El diccionario facilitó la relación entre las opciones seleccionadas por el usuario y las funciones del programa. Finalmente, el conjunto permitió obtener las categorías de los productos sin duplicados.

Además, mantener separadas las clases de los modelos, el servicio `Restaurante` y el archivo `main.py` permite que el proyecto tenga una estructura más organizada y fácil de mantener.

La correcta selección de estructuras de datos permite desarrollar soluciones más claras, reutilizables y adaptadas a las necesidades del sistema.

---

# 👨‍💻 Autor

**Clide  Alvarado **

**Programación Orientada a Objetos**

**Tarea Semana 9**

---

## 📚 Tecnologías utilizadas

* Python
* Programación Orientada a Objetos
* Listas (`list`)
* Tuplas (`tuple`)
* Diccionarios (`dict`)
* Conjuntos (`set`)
* Visual Studio Code
* GitHub
