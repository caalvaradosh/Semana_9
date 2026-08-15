from collections.abc import Callable

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# =========================================================
# TUPLA
# =========================================================
# Las opciones del menú son información estable durante
# la ejecución del programa.

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


# =========================================================
# MOSTRAR MENÚ
# =========================================================

def mostrar_menu() -> None:
    """
    Muestra el menú principal.
    """
    print("\n")
    print("=" * 50)
    print("          SISTEMA DE RESTAURANTE El BamBú ")
    print("=" * 50)

    for numero, opcion in enumerate(
        OPCIONES_MENU,
        start=1
    ):
        print(f"{numero}. {opcion}")

    print("=" * 50)


# =========================================================
# VALIDACIÓN DE TEXTO
# =========================================================

def leer_texto(mensaje: str) -> str:
    """
    Solicita un texto no vacío.
    """
    while True:
        valor = input(mensaje).strip()

        if valor:
            return valor

        print(
            "ERROR: El campo no puede quedar vacío."
        )


# =========================================================
# VALIDACIÓN DE PRECIO
# =========================================================

def leer_precio() -> float:
    """
    Solicita un precio válido.
    """
    while True:
        try:
            precio = float(
                input("Precio: $").strip()
            )

            if precio <= 0:
                print(
                    "ERROR: El precio debe ser mayor que cero."
                )
                continue

            return precio

        except ValueError:
            print(
                "ERROR: Ingrese un precio numérico válido."
            )


# =========================================================
# 1. REGISTRAR PRODUCTO
# =========================================================

def registrar_producto(
    restaurante: Restaurante
) -> None:
    """
    Registra un nuevo producto.
    """
    print("\n")
    print("=" * 50)
    print("          REGISTRAR PRODUCTO")
    print("=" * 50)

    codigo = leer_texto("Código: ")

    if restaurante.existe_codigo(codigo):
        print(
            "\nERROR: Ya existe un producto "
            "con ese código."
        )
        return

    nombre = leer_texto("Nombre: ")
    categoria = leer_texto("Categoría: ")
    precio = leer_precio()

    producto = Producto(
        codigo=codigo,
        nombre=nombre,
        categoria=categoria,
        precio=precio
    )

    registrado = restaurante.registrar_producto(
        producto
    )

    if registrado:
        print(
            "\nProducto registrado correctamente."
        )
    else:
        print(
            "\nERROR: No fue posible registrar "
            "el producto."
        )


# =========================================================
# 2. BUSCAR PRODUCTO
# =========================================================

def buscar_producto(
    restaurante: Restaurante
) -> None:
    """
    Busca un producto por código.
    """
    print("\n")
    print("=" * 50)
    print("            BUSCAR PRODUCTO")
    print("=" * 50)

    codigo = leer_texto(
        "Ingrese el código del producto: "
    )

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print(
            "\nNo se encontró ningún producto "
            "con ese código."
        )
        return

    print("\nProducto encontrado:")
    print("-" * 50)
    print(producto.mostrar_informacion())


# =========================================================
# 3. ACTUALIZAR PRODUCTO
# =========================================================

def actualizar_producto(
    restaurante: Restaurante
) -> None:
    """
    Actualiza un producto existente.
    """
    print("\n")
    print("=" * 50)
    print("          ACTUALIZAR PRODUCTO")
    print("=" * 50)

    codigo = leer_texto(
        "Código del producto: "
    )

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print(
            "\nNo se encontró ningún producto "
            "con ese código."
        )
        return

    print("\nInformación actual:")
    print("-" * 50)
    print(producto.mostrar_informacion())

    print("\nIngrese los nuevos datos:")

    nombre = leer_texto(
        "Nuevo nombre: "
    )

    categoria = leer_texto(
        "Nueva categoría: "
    )

    precio = leer_precio()

    try:
        actualizado = restaurante.actualizar_producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio
        )

        if actualizado:
            print(
                "\nProducto actualizado correctamente."
            )
        else:
            print(
                "\nNo fue posible actualizar "
                "el producto."
            )

    except ValueError as error:
        print(f"\nERROR: {error}")


# =========================================================
# 4. ELIMINAR PRODUCTO
# =========================================================

def eliminar_producto(
    restaurante: Restaurante
) -> None:
    """
    Elimina un producto por código.
    """
    print("\n")
    print("=" * 50)
    print("           ELIMINAR PRODUCTO")
    print("=" * 50)

    codigo = leer_texto(
        "Código del producto: "
    )

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print(
            "\nNo se encontró ningún producto "
            "con ese código."
        )
        return

    print("\nProducto encontrado:")
    print("-" * 50)
    print(producto.mostrar_informacion())

    confirmacion = input(
        "\n¿Está seguro de eliminar este producto? "
        "(s/n): "
    ).strip().lower()

    if confirmacion != "s":
        print("\nOperación cancelada.")
        return

    eliminado = restaurante.eliminar_producto(
        codigo
    )

    if eliminado:
        print(
            "\nProducto eliminado correctamente."
        )
    else:
        print(
            "\nNo fue posible eliminar "
            "el producto."
        )


# =========================================================
# 5. LISTAR PRODUCTOS
# =========================================================

def listar_productos(
    restaurante: Restaurante
) -> None:
    """
    Muestra todos los productos registrados.
    """
    print("\n")
    print("=" * 50)
    print("            LISTA DE PRODUCTOS")
    print("=" * 50)

    productos = restaurante.listar_productos()

    if not productos:
        print(
            "\nNo existen productos registrados."
        )
        return

    for numero, producto in enumerate(
        productos,
        start=1
    ):
        print(f"\nProducto #{numero}")
        print("-" * 50)
        print(producto.mostrar_informacion())

    print("\n" + "=" * 50)
    print(
        f"Total de productos: {len(productos)}"
    )


# =========================================================
# 6. REGISTRAR USUARIO
# =========================================================

def registrar_usuario(
    restaurante: Restaurante
) -> None:
    """
    Registra un nuevo usuario.
    """
    print("\n")
    print("=" * 50)
    print("            REGISTRAR USUARIO")
    print("=" * 50)

    identificacion = leer_texto(
        "Identificación: "
    )

    if restaurante.existe_identificacion(
        identificacion
    ):
        print(
            "\nERROR: Ya existe un usuario "
            "con esa identificación."
        )
        return

    nombre = leer_texto(
        "Nombre: "
    )

    correo = leer_texto(
        "Correo electrónico: "
    )

    usuario = Usuario(
        identificacion=identificacion,
        nombre=nombre,
        correo=correo
    )

    registrado = restaurante.registrar_usuario(
        usuario
    )

    if registrado:
        print(
            "\nUsuario registrado correctamente."
        )
    else:
        print(
            "\nERROR: No fue posible registrar "
            "el usuario."
        )


# =========================================================
# 7. LISTAR USUARIOS
# =========================================================

def listar_usuarios(
    restaurante: Restaurante
) -> None:
    """
    Muestra todos los usuarios registrados.
    """
    print("\n")
    print("=" * 50)
    print("             LISTA DE USUARIOS")
    print("=" * 50)

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print(
            "\nNo existen usuarios registrados."
        )
        return

    for numero, usuario in enumerate(
        usuarios,
        start=1
    ):
        print(f"\nUsuario #{numero}")
        print("-" * 50)
        print(usuario.mostrar_informacion())

    print("\n" + "=" * 50)
    print(
        f"Total de usuarios: {len(usuarios)}"
    )


# =========================================================
# 8. MOSTRAR CATEGORÍAS
# =========================================================

def mostrar_categorias(
    restaurante: Restaurante
) -> None:
    """
    Muestra las categorías únicas de los productos.
    """
    print("\n")
    print("=" * 50)
    print("        CATEGORÍAS DE PRODUCTOS")
    print("=" * 50)

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print(
            "\nNo existen categorías registradas."
        )
        return

    print(
        "\nCategorías disponibles:"
    )

    for categoria in sorted(categorias):
        print(f"- {categoria}")

    print(
        f"\nTotal de categorías únicas: "
        f"{len(categorias)}"
    )


# =========================================================
# 9. SALIR
# =========================================================

def salir(
    restaurante: Restaurante
) -> bool:
    """
    Finaliza el programa.
    """
    print("\n")
    print("=" * 50)
    print(
        "Gracias por utilizar el "
        "Sistema de Restaurante."
    )
    print("=" * 50)

    return False


# =========================================================
# DICCIONARIO
# =========================================================
# Relaciona cada opción del menú con una función.

def ejecutar() -> None:
    """
    Ejecuta el programa principal.
    """
    restaurante = Restaurante()

    acciones: dict[
        str,
        Callable[[], None]
    ] = {
        "1": lambda: registrar_producto(
            restaurante
        ),
        "2": lambda: buscar_producto(
            restaurante
        ),
        "3": lambda: actualizar_producto(
            restaurante
        ),
        "4": lambda: eliminar_producto(
            restaurante
        ),
        "5": lambda: listar_productos(
            restaurante
        ),
        "6": lambda: registrar_usuario(
            restaurante
        ),
        "7": lambda: listar_usuarios(
            restaurante
        ),
        "8": lambda: mostrar_categorias(
            restaurante
        ),
    }

    continuar = True

    while continuar:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "9":
            continuar = salir(restaurante)
            continue

        accion = acciones.get(opcion)

        if accion is None:
            print(
                "\nERROR: Opción no válida."
            )
            continue

        try:
            accion()

        except ValueError as error:
            print(
                f"\nERROR DE VALIDACIÓN: {error}"
            )

        except Exception as error:
            print(
                f"\nERROR INESPERADO: {error}"
            )


# =========================================================
# PUNTO DE ENTRADA
# =========================================================

if __name__ == "__main__":
    ejecutar()