from abc import ABC, abstractmethod, abstractproperty
from Interprete.ast.nodo import Nodo


class Instruccion(ABC):
    @property
    def controlador(self):
        pass

    @property
    def tabla_simbolos(self):
        pass

    @abstractmethod
    def ejecutar(self, controlador, ts):
        pass

    def recorrer(self) -> Nodo:
        pass
