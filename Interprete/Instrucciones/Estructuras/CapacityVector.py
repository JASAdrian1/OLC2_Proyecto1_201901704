from Interprete.Interfaces.Expresion import Expresion
from Interprete.TablaSimbolos.Error import Error
from Interprete.TablaSimbolos.Tipo import tipo
from Interprete.ast.nodo import Nodo


class CapacityVector(Expresion):
    def __init__(self,id,linea,columna):
        self.id = id
        self.linea = linea
        self.columna = columna

    def getTipo(self, controlador, ts) -> tipo:
        return tipo.I64

    def getValor(self, contralador, ts):
        variable = ts.getSimbolo(self.id)
        if variable is not None:
            if variable.tipoDato.tipo_enum == tipo.VEC:
                print("Retornando len")
                print(variable.valor)
                return len(variable.valor.expresion)
            else:
                contralador.agregarAConsola(
                    "***ERROR***No se esta usando el comando push en un vector. Linea: %d Columna: %d" % (
                    self.linea, self.columna))
                contralador.agregarError(
                    Error("SEMANTICO", "No se esta usando el comando push en un vector", self.linea,
                          self.columna))
        else:
            contralador.agregarAConsola(
                "***ERROR***La variable no exite. Linea: %d Columna: %d" % (self.linea, self.columna))
            contralador.agregarError(
                Error("SEMANTICO", "Variable no existe", self.linea,
                      self.columna))

    def recorrer(self) -> Nodo:
        pass