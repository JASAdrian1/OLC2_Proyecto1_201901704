from Interprete.Interfaces.Expresion import Expresion
from Interprete.TablaSimbolos.Error import Error
from Interprete.TablaSimbolos.Tipo import Tipo
from Interprete.TablaSimbolos.Tipo import tipo
from Interprete.ast.nodo import Nodo


class Identificador(Expresion):
    def __init__(self, id, linea, columna):
        self.id = id
        self.linea = linea
        self.columna = columna

    def getValor(self, contralador, ts):
        variable = ts.getSimbolo(self.id)
        if variable is not None:
            return variable.valor
        else:
            contralador.agregarAConsola("***ERROR***LA variable con el id %s no ha sido declarado" % self.id)
            contralador.agregarError(Error("SEMANTICO",
                                           "LA variable con el id "+ self.id + " no ha sido declarado",self.linea, self.columna))

    def getTipo(self, controlador, ts) -> tipo:
        variable = ts.getSimbolo(self.id)
        if variable is not None:
            print(variable.valor,"/----------------------")
            print(variable.tipoDato)
            print(self.linea)
            return variable.tipoDato.tipo_enum
        else:
            controlador.agregarAConsola("***ERROR***LA variable con el id %s no ha sido declarado" % self.id)
            controlador.agregarError(Error("SEMANTICO",
                                           "LA variable con el id " + self.id + " no ha sido declarado", self.linea,
                                           self.columna))
            return tipo.ERROR

    def getEstructuraArreglo(self,controlador,ts):
        variable = ts.getSimbolo(self.id)
        if variable.tipoDato.tipo_enum == tipo.ARRAY:
            if variable is not None:
                return variable.estructuraArr
            else:
                print("No se ha devuleto nada en getEstructuraArreglo (identificador)")
        else:
            print("No se ha devuleto nada en getEstructuraArreglo (identificador)")

    def getTipoElementosArreglo(self,controlador,ts):
        variable = ts.getSimbolo(self.id)
        if variable.tipoDato.tipo_enum == tipo.ARRAY:
            if variable is not None:
                return variable.tipoElementosArray
            else:
                print("No se ha devuleto nada en getTipoElementosArreglo (identificador)")
        else:
            print("No se ha devuleto nada en getTipoElementosArreglo (identificador)")

    def recorrer(self) -> Nodo:
        pass