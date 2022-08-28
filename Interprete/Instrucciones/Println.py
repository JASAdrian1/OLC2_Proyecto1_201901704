from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.ast.nodo import Nodo
from Interprete.TablaSimbolos.Error import Error
import re


class Pritnln(Instruccion):
    def __init__(self, cadena, valores, linea, columna):
        self.cadena = cadena
        self.valores = valores
        self.linea = linea
        self.columna = columna
        self.tipoInstruccion="print"


    def ejecutar(self, controlador, ts):
        if self.valores is not None:
            llaves_cadena = re.findall(r'{.*}',self.cadena)
            #print("***",self.cadena)
            if len(self.valores) == len(llaves_cadena):
                #print("///",len(llaves_cadena))
                for valor in self.valores:
                    nueva_cadena = re.sub(r'{.*}',str(valor.getValor(controlador,ts)),self.cadena,1)
                    controlador.agregarAConsola(nueva_cadena)
                controlador.agregarAConsola("\n")
            else:
                controlador.agregarAConsola("***ERROR***La cantidad de llaves no coinciden los valores a imprimir")
                controlador.agregarError(Error("SEMANTICO","La cantidad de llaves no coinciden los valores a imprimir",self.linea,self.columna))
        else:
            controlador.agregarAConsola(self.cadena)
            controlador.agregarAConsola("\n")


    def recorrer(self) -> Nodo:
        pass