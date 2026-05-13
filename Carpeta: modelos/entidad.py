modelos/
│
├── entidad.py
├── cliente.py
├── servicio.py
├── servicios_especializados.py
└── reserva.py
from abc import ABC, abstractmethod

class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass
      
