from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self) -> None:
        # LISTAS:
        # Se utilizan para almacenar las colecciones dinámicas
        # de productos y usuarios.
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

    # ==========================================================
    # PRODUCTOS
    # ==========================================================

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un producto si su código no está repetido.
        """
        if self.buscar_producto(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        """
        Busca un producto utilizando su código.
        """
        codigo = codigo.strip()

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
    ) -> bool:
        """
        Actualiza los datos de un producto existente.
        """
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """
        Elimina un producto utilizando su código.
        """
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        """
        Devuelve una copia de la lista de productos.
        """
        return self._productos.copy()

    def contar_productos(self) -> int:
        """
        Retorna la cantidad de productos registrados.
        """
        return len(self._productos)

    # ==========================================================
    # USUARIOS
    # ==========================================================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Registra un usuario si su identificación no está repetida.
        """
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False

        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        """
        Busca un usuario mediante su identificación.
        """
        identificacion = identificacion.strip()

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:
        """
        Devuelve una copia de la lista de usuarios.
        """
        return self._usuarios.copy()

    def contar_usuarios(self) -> int:
        """
        Retorna la cantidad de usuarios registrados.
        """
        return len(self._usuarios)

    # ==========================================================
    # CONJUNTO - CATEGORÍAS ÚNICAS
    # ==========================================================

    def obtener_categorias_unicas(self) -> set[str]:
        """
        Obtiene las categorías de los productos sin repetir.
        """
        categorias: set[str] = set()

        for producto in self._productos:
            categorias.add(producto.categoria)

        return categorias

    def existe_categoria(self, categoria: str) -> bool:
        """
        Comprueba si una categoría existe.
        """
        return categoria.strip() in self.obtener_categorias_unicas()