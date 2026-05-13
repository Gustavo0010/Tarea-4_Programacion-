class Reserva:

    def __init__(self, cliente, servicio):

        if cliente is None:
            raise ValueError("Cliente inválido")

        if servicio is None:
            raise ValueError("Servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_pago(self):

        try:
            costo = self.servicio.calcular_costo()

        except Exception as e:
            raise Exception("Error procesando pago") from e

        return costo
