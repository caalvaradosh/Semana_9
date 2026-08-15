class Cliente:
    """
    Representa un cliente del restaurante.
    """

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo

    @property
    def identificacion(self) -> str:
        return self.__identificacion

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def correo(self) -> str:
        return self.__correo

    def mostrar_informacion(self) -> str:
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}"
        )