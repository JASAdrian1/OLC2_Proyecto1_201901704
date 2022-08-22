from Interprete.Interfaces.Instruccion import Instruccion


class BrazoMatch(Instruccion):
    def __init__(self, condiciones, instrucciones, linea, columna):
        self.condiciones = condiciones
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna


    def ejecutar(self, controlador, ts):
        #print(self.instrucciones)
        for instruccion in self.instrucciones:
            instruccion.ejecutar(controlador, ts)
