from Interprete.Expresiones.InicializacionVector import InicializacionVector
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
            copia_cadena_original = self.cadena
            llaves_cadena = re.findall(r'{}',self.cadena)
            llaves_cadena_array = re.findall(r'{:\?}',self.cadena)
            print("***",self.cadena)
            print("Comprobando llaves en impresion: ",len(self.valores), " == ", str(len(llaves_cadena)+len(llaves_cadena_array)))
            if len(self.valores) == len(llaves_cadena) + len(llaves_cadena_array):
                #print("///",len(llaves_cadena))
                for valor in self.valores:
                    if isinstance(valor.getValor(controlador,ts),InicializacionVector):
                        cadenaAImprimir = "["
                        for elemento in valor.getValor(controlador,ts).expresion:
                            cadenaAImprimir += str(elemento.getValor(controlador,ts))+","
                        cadenaAImprimir = cadenaAImprimir[:-1]          #Se elimina la ultima coma puesta en el ciclo
                        cadenaAImprimir += "]"
                        nueva_cadena = re.sub(r'{:\?}', cadenaAImprimir, self.cadena, 1)
                    else:
                        nueva_cadena = re.sub(r'{}',str(valor.getValor(controlador,ts)),self.cadena,1)
                    self.cadena = nueva_cadena
                controlador.agregarAConsola(nueva_cadena)
                controlador.agregarAConsola("\n")
                self.cadena = copia_cadena_original
            else:
                controlador.agregarAConsola("***ERROR***La cantidad de llaves no coinciden los valores a imprimir")
                controlador.agregarError(Error("SEMANTICO","La cantidad de llaves no coinciden los valores a imprimir",self.linea,self.columna))
        else:
            controlador.agregarAConsola(self.cadena)
            controlador.agregarAConsola("\n")


    def recorrer(self) -> Nodo:
        pass