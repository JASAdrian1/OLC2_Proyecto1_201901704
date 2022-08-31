from Interprete.Interfaces.Expresion import Expresion
from Interprete.TablaSimbolos.Error import Error
from Interprete.TablaSimbolos.Tipo import  tipo
from Interprete.ast.nodo import Nodo


class ContainsVector(Expresion):
    def __init__(self,id,expresion,linea,columna):
        self.id = id
        self.expresion = expresion
        self.linea = linea
        self.columna = columna


    def getTipo(self, controlador, ts) -> tipo:
        return tipo.BOOL

    def getValor(self, contralador, ts):
        variable = ts.getSimbolo(self.id)
        if variable is not None:
            if variable.esMutable is True:
                if variable.tipoDato == "VEC":
                    for elemento in variable.valor.expresion:
                        if elemento.getValor(contralador,ts) == self.expresion.getValor(contralador,ts):
                            return "true"
                    return "false"
                else:
                    contralador.agregarAConsola("***ERROR***No se esta usando el comando push en un vector. Linea: %d Columna: %d" % (self.linea, self.columna))
                    contralador.agregarError(
                        Error("SEMANTICO", "No se esta usando el comando push en un vector", self.linea,
                              self.columna))
            else:
                contralador.agregarAConsola("***ERROR***El vector es no mutable. Linea: %d Columna: %d" % (self.linea, self.columna))
                contralador.agregarError(
                    Error("SEMANTICO", "El vector es no mutable", self.linea,
                          self.columna))
        else:
            contralador.agregarAConsola("***ERROR***La variable con id ", self.id, " no exite. Linea: %d Columna: %d" % (self.linea, self.columna))
            contralador.agregarError(
                Error("SEMANTICO", "Variable no existe", self.linea,
                      self.columna))

    def recorrer(self) -> Nodo:
        pass
