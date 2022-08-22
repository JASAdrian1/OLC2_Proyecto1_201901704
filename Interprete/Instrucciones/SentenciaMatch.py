from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.Error import Error


class SentenciaMatch(Instruccion):
    def __init__(self, condicion, listaBrazos, brazoDefault, linea, columna):
        self.condicion = condicion
        self.listaBrazos = listaBrazos
        self.brazoDefault = brazoDefault
        self.seEjecutaDefault = True
        self.linea = linea
        self.columna = columna


    def ejecutar(self, controlador, ts):
        condicionMatch = self.condicion.getValor(controlador,ts)
        condicionTipo = self.condicion.getTipo(controlador,ts)
        for brazo in self.listaBrazos:
            for condicion in brazo.condiciones:
                if condicionTipo == condicion.getTipo(controlador,ts):
                    if condicionMatch == condicion.getValor(controlador,ts):
                        brazo.ejecutar(controlador,ts)
                        self.seEjecutaDefault = False
                else:
                    print("***ERROR***El tipo de la condición del brazo no coincide con el tipo de la condicion del match")
                    controlador.agregarAConsola("***ERROR***El tipo de la condición del brazo no coincide con el tipo de la condicion del match")
                    controlador.agregarError(Error("SEMANTICO","El tipo de la condición del brazo no coincide con el tipo de la condicion del match",self.columna,self.linea))
                    break

        if self.seEjecutaDefault == True:
            if self.brazoDefault != None:
                self.brazoDefault.ejecutar(controlador,ts)
