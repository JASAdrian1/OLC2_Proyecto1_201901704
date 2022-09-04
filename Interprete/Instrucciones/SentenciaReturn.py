from Interprete.Interfaces.Instruccion import Instruccion


class SentenciaReturn(Instruccion):
    def __init__(self, valorRetorno,linea, columna):
        self.valorRetorno = valorRetorno
        self.linea = linea
        self.columna = columna

    def ejecutar(self, controlador, ts):
        if self.valorRetorno is None:
            return self
        else:
            return self.valorRetorno.getValor(controlador,ts)