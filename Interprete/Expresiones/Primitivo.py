from Interprete.Interfaces.Expresion import Expresion
from Interprete.TablaSimbolos.Tipo import Tipo,tipo
from Interprete.ast.nodo import Nodo


class Primitivo(Expresion):
    def __init__(self, valor, type, linea, columna):
        self.valor = valor
        self.tipo = Tipo(type)
        self.linea = linea
        self.columna = columna

    def getTipo(self, controlador, ts) -> tipo:
        return  self.tipo.tipo_enum

    def getValor(self, contralador, ts):
        return self.valor

    def recorrer(self) -> Nodo:
        pass
