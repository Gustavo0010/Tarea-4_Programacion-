from modelos.servicio import Servicio

class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, horas):
        super().__init__(nombre, precio_base)
        self.horas = horas

    def calcular_costo(self):
        return self.precio_base * self.horas

    def descripcion(self):
        return "Reserva de sala empresarial"


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, dias):
        super().__init__(nombre, precio_base)
        self.dias = dias

    def calcular_costo(self):
        return self.precio_base * self.dias

    def descripcion(self):
        return "Alquiler de equipos tecnológicos"


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, nivel):
        super().__init__(nombre, precio_base)
        self.nivel = nivel

    def calcular_costo(self):

        if self.nivel == "avanzada":
            return self.precio_base * 2

        return self.precio_base

    def descripcion(self):
        return "Asesoría especializada"
