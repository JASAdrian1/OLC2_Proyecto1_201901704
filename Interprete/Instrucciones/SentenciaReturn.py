from Interprete.Interfaces.Instruccion import Instruccion


class SentenciaReturn(Instruccion):
    def __init__(self, valorRetorno,linea, columna):
        self.valorRetorno = valorRetorno
        self.linea = linea
        self.columna = columna

    def ejecutar(self, controlador, ts):
        print("Hay un return")
        print(self.valorRetorno)
        return self