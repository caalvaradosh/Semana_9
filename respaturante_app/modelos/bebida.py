from .producto import Producto


class Bebida(Producto):
    """
    Representa una bebida del restaurante.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        tamaño: str
    ) -> None:
        super().__init__(
            codigo,
            nombre,
            "Bebida",
            precio
        )
        self.__tamaño = tamaño

    @property
    def tamaño(self) -> str:
        return self.__tamaño

    def mostrar_informacion(self) -> str:
        return (
            f"{super().mostrar_informacion()}\n"
            f"Tamaño: {self.tamaño}"
        )