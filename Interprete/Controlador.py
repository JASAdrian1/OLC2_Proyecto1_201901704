

class Controlador:
    def __init__(self):
        self.errs = []
        self.consola = ""
        self.esCiclo = False

    def agregarError(self,error):
        self.errs.append(error)

    def agregarAConsola(self,cadena):
        if cadena[0] == "\"" and cadena[len(cadena)-1]:
            self.consola += cadena[1:-1]
        else:
            self.consola += cadena