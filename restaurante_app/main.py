from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# ==========================================================
# TUPLA
# ==========================================================
# La tupla contiene las opciones estables del menú.
# Se utiliza porque estas opciones no necesitan modificarse
# durante la ejecución del programa.

OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar usuarios"),
    ("8", "Mostrar categorías"),
    ("9", "Salir"),
)


# ==========================================================
# FUNCIONES GENERALES
# ==========================================================

def pedir_texto(mensaje: str) -> str:
    """
    Solicita un texto al usuario.
    """
    return input(mensaje).strip()


def pedir_precio(mensaje: str) -> float:
    """
    Solicita un precio y valida que sea un número positivo
    o cero.
    """
    while True:
        try:
            precio = float(input(mensaje))

            if precio < 0:
                print("El precio no puede ser negativo.")
                continue

            return precio

        except ValueError:
            print("Ingrese un precio válido. Ejemplo: 5.50")


def mostrar_menu() -> None:
    """
    Muestra las opciones del menú principal.
    """
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE EL BAMBÚ DE COTUNDO")
    print("========================================")

    for numero, descripcion in OPCIONES_MENU:
        print(f"{numero}. {descripcion}")

    print("========================================")


# ==========================================================
# PRODUCTOS
# ==========================================================

def registrar_producto(restaurante: Restaurante) -> None:
    """
    Solicita los datos y registra un producto.
    """
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = pedir_texto("Código: ")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoría: ")
    precio = pedir_precio("Precio: ")

    try:
        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
        )

        registrado = restaurante.registrar_producto(producto)

        if registrado:
            print("Producto registrado correctamente.")
        else:
            print("Error: el código del producto ya está registrado.")

    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto(restaurante: Restaurante) -> None:
    """
    Busca un producto mediante su código.
    """
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = pedir_texto("Código del producto: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print("\nProducto encontrado:")
        print(producto)


def actualizar_producto(restaurante: Restaurante) -> None:
    """
    Actualiza un producto existente.
    """
    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = pedir_texto("Código del producto: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"\nProducto actual: {producto}")

    nuevo_nombre = pedir_texto("Nuevo nombre: ")
    nueva_categoria = pedir_texto("Nueva categoría: ")
    nuevo_precio = pedir_precio("Nuevo precio: ")

    try:
        actualizado = restaurante.actualizar_producto(
            codigo,
            nuevo_nombre,
            nueva_categoria,
            nuevo_precio,
        )

        if actualizado:
            print("Producto actualizado correctamente.")
        else:
            print("No fue posible actualizar el producto.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(restaurante: Restaurante) -> None:
    """
    Elimina un producto utilizando su código.
    """
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = pedir_texto("Código del producto: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"\nProducto seleccionado: {producto}")

    confirmacion = pedir_texto(
        "¿Está seguro de eliminarlo? (s/n): "
    ).lower()

    if confirmacion != "s":
        print("Operación cancelada.")
        return

    eliminado = restaurante.eliminar_producto(codigo)

    if eliminado:
        print("Producto eliminado correctamente.")
    else:
        print("No fue posible eliminar el producto.")


def listar_productos(restaurante: Restaurante) -> None:
    """
    Muestra todos los productos registrados.
    """
    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for indice, producto in enumerate(productos, start=1):
        print(f"{indice}. {producto}")

    print(f"\nTotal de productos: {restaurante.contar_productos()}")


# ==========================================================
# USUARIOS
# ==========================================================

def registrar_usuario(restaurante: Restaurante) -> None:
    """
    Solicita los datos y registra un usuario.
    """
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = pedir_texto("Identificación: ")
    nombre = pedir_texto("Nombre: ")
    correo = pedir_texto("Correo electrónico: ")

    try:
        usuario = Usuario(
            identificacion,
            nombre,
            correo,
        )

        registrado = restaurante.registrar_usuario(usuario)

        if registrado:
            print("Usuario registrado correctamente.")
        else:
            print(
                "Error: la identificación del usuario "
                "ya está registrada."
            )

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(restaurante: Restaurante) -> None:
    """
    Muestra todos los usuarios registrados.
    """
    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    for indice, usuario in enumerate(usuarios, start=1):
        print(f"{indice}. {usuario}")

    print(f"\nTotal de usuarios: {restaurante.contar_usuarios()}")


# ==========================================================
# CATEGORÍAS
# ==========================================================

def mostrar_categorias(restaurante: Restaurante) -> None:
    """
    Muestra las categorías de productos sin duplicados.
    """
    print("\n--- CATEGORÍAS ÚNICAS ---")

    categorias = restaurante.obtener_categorias_unicas()

    if len(categorias) == 0:
        print("No hay categorías registradas.")
        return

    print("Categorías disponibles:")

    for categoria in sorted(categorias):
        print(f"- {categoria}")

    categoria_consultada = pedir_texto(
        "\nConsultar una categoría "
        "(presione Enter para omitir): "
    )

    if categoria_consultada:
        if restaurante.existe_categoria(categoria_consultada):
            print("La categoría existe.")
        else:
            print("La categoría no existe.")


# ==========================================================
# EJECUCIÓN DEL MENÚ
# ==========================================================

def ejecutar_menu() -> None:
    """
    Ejecuta el menú principal del sistema.
    """

    restaurante = Restaurante()

    # ======================================================
    # DICCIONARIO
    # ======================================================
    # Relaciona cada opción del menú con la función
    # correspondiente.
    opciones = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
    }

    while True:
        mostrar_menu()

        opcion = pedir_texto(
            "Seleccione una opción: "
        )

        if opcion == "9":
            print("\nGracias por utilizar el Sistema de Restaurante.")
            print("Programa finalizado.")
            break

        accion = opciones.get(opcion)

        if accion is None:
            print("Opción inválida. Seleccione una opción del menú.")
            continue

        accion(restaurante)


# ==========================================================
# PUNTO DE ENTRADA
# ==========================================================

if __name__ == "__main__":
    ejecutar_menu()