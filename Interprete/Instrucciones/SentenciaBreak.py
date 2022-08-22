from Interprete.Interfaces.Instruccion import Instruccion


class SentenciaBreak(Instruccion):
    def __init__(self):
        self.tipoInstruccion = "break"


    def ejecutar(self, controlador, ts):
        #print("AAasdasdasdasdasdsadasd")
        #print("--",self)
        return self
