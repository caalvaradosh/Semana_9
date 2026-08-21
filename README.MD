# Restaurante App - Semana 9

## Programación Orientada a Objetos

**Estudiante:** Clide Alvarado

**Actividad:** Semana 9 - Estructuras de datos aplicadas al proyecto restaurante_app

---

## 1. Descripción del proyecto

Restaurante App es un sistema desarrollado en Python para administrar de manera básica los productos y usuarios de un restaurante.

El proyecto utiliza programación orientada a objetos y estructuras de datos de Python para organizar la información y realizar diferentes operaciones mediante un menú interactivo por consola.

El sistema permite:

- Registrar productos.
- Buscar productos por código.
- Actualizar productos.
- Eliminar productos.
- Listar productos.
- Registrar usuarios.
- Listar usuarios.
- Mostrar categorías de productos sin duplicados.
- Evitar códigos de productos repetidos.
- Evitar identificaciones de usuarios repetidas.

---

## 2. Objetivo

El objetivo principal de esta actividad es aplicar de manera funcional las principales estructuras de datos de Python:

- Listas (`list`)
- Tuplas (`tuple`)
- Diccionarios (`dict`)
- Conjuntos (`set`)

Cada estructura se utiliza para resolver una necesidad concreta dentro del sistema.

---

## 3. Estructura del proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
│
└── README.md