from abc import ABC, abstractmethod
from Interprete.TablaSimbolos import Tipo, TablaSimbolos
from Interprete.ast.nodo import Nodo


class Expresion(ABC):
    @abstractmethod
    def getTipo(self, controlador, ts) -> Tipo.tipo:
        pass

    @abstractmethod
    def getValor(self, contralador, ts):
        pass

    @abstractmethod
    def recorrer(self) -> Nodo:
        pass
