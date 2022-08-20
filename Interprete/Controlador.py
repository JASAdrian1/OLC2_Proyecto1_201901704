

class Controlador:
    def __init__(self):
        self.errs = []
        self.consola = ""
        self.esCiclo = False

    def agregarError(self,error):
        self.errs.append(error)

    def agregarAConsola(self,cadena):
        self.consola += cadena