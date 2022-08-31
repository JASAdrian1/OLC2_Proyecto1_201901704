from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.Error import Error


class RemoveVector(Instruccion):
    def __init__(self, id, posicion, linea, columna):
        self.id = id
        self.posicion = posicion
        self.linea = linea
        self.columna = columna


    def ejecutar(self, controlador, ts):
        variable = ts.getSimbolo(self.id)
        if variable is not None:
            if variable.esMutable is True:
                if variable.tipoDato == "VEC":
                    if self.posicion.getValor(controlador,ts) < len(variable.valor.expresion) and self.posicion.getValor(controlador,ts) >=0:
                        variable.valor.expresion.pop(self.posicion.getValor(controlador,ts))
                    else:
                        controlador.agregarAConsola("***ERROR***Limite fuera del vector. Linea: %d Columna: %d" % (self.linea, self.columna))
                        controlador.agregarError( Error("SEMANTICO", "Limite fuera del vector. Linea",self.linea,self.columna))
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
            controlador.agregarAConsola("***ERROR***La variable con id: %s no exite. Linea: %d Columna: %d" % (self.id,self.linea, self.columna))
            controlador.agregarError(
                Error("SEMANTICO", "Variable no existe", self.linea,
                      self.columna))