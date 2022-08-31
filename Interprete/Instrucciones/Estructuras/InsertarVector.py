from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.Error import Error


class InsertarVector(Instruccion):
    def __init__(self,id,posicion,valor,linea,columna):
        self.id = id
        self.posicion = posicion
        self.valor = valor
        self.linea = linea
        self.columna = columna

    def ejecutar(self, controlador, ts):
        variable = ts.getSimbolo(self.id)
        tipoNuevoValor = self.valor.getTipo(controlador, ts)
        if variable is not None:
            print("HOLA??????????????????????")
            if variable.esMutable is True:
                if variable.tipoDato == "VEC":
                    variable.valor.expresion[self.posicion.getValor(controlador,ts)] = self.valor
                else:
                    controlador.agregarAConsola("***ERROR***No se esta usando el comando push en un vector. Linea: %d Columna: %d" % (self.linea, self.columna))
                    controlador.agregarError(
                        Error("SEMANTICO", "No se esta usando el comando push en un vector", self.linea,
                              self.columna))
            else:
                controlador.agregarAConsola("***ERROR***El vector es no mutable. Linea: %d Columna: %d" % (self.linea, self.columna))
                controlador.agregarError(
                    Error("SEMANTICO", "El vector es no mutable", self.linea,
                          self.columna))
        else:
            controlador.agregarAConsola("***ERROR***La variable con id ", self.id, " no exite. Linea: %d Columna: %d" % (self.linea, self.columna))
            controlador.agregarError(
                Error("SEMANTICO", "Variable no existe", self.linea,
                      self.columna))