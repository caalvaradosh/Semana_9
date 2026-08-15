from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """
    Servicio encargado de administrar productos y usuarios.
    """

    def __init__(self) -> None:
        # LISTAS:
        # Se utilizan para almacenar colecciones dinámicas.
        self.__productos: list[Producto] = []
        self.__usuarios: list[Usuario] = []

    # =====================================================
    # VALIDACIONES
    # =====================================================

    def existe_codigo(self, codigo: str) -> bool:
        """
        Comprueba si ya existe un producto con el código indicado.
        """
        return any(
            producto.codigo == codigo
            for producto in self.__productos
        )

    def existe_identificacion(
        self,
        identificacion: str
    ) -> bool:
        """
        Comprueba si ya existe un usuario con la
        identificación indicada.
        """
        return any(
            usuario.identificacion == identificacion
            for usuario in self.__usuarios
        )

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def registrar_producto(
        self,
        producto: Producto
    ) -> bool:
        """
        Registra un producto evitando códigos duplicados.
        """
        if self.existe_codigo(producto.codigo):
            return False

        self.__productos.append(producto)
        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:
        """
        Busca un producto mediante su código.
        """
        for producto in self.__productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:
        """
        Actualiza los datos de un producto existente.
        """
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        return True

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:
        """
        Elimina un producto mediante su código.
        """
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.__productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        """
        Devuelve una copia de la lista de productos.
        """
        return self.__productos.copy()

    # =====================================================
    # USUARIOS
    # =====================================================

    def registrar_usuario(
        self,
        usuario: Usuario
    ) -> bool:
        """
        Registra un usuario evitando identificaciones duplicadas.
        """
        if self.existe_identificacion(
            usuario.identificacion
        ):
            return False

        self.__usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> list[Usuario]:
        """
        Devuelve una copia de la lista de usuarios.
        """
        return self.__usuarios.copy()

    # =====================================================
    # CONJUNTO
    # =====================================================

    def obtener_categorias(self) -> set[str]:
        """
        Obtiene las categorías únicas de los productos.

        SET:
        Se utiliza para evitar categorías duplicadas.
        """
        return {
            producto.categoria
            for producto in self.__productos
        }