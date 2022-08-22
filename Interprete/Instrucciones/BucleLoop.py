from Interprete.Instrucciones.SentenciaBreak import SentenciaBreak
from Interprete.Interfaces.Instruccion import Instruccion
import inspect

from Interprete.TablaSimbolos.TablaSimbolos import TablaSimbolos


class BucleLoop(Instruccion):
    def __init__(self, listaInstrucciones):
        self.listaInstrucciones = listaInstrucciones


    def ejecutar(self, controlador, ts):
        esBreak = False
        while esBreak is False:
            tablaLocal = TablaSimbolos(ts)
            for instruccion in self.listaInstrucciones:
                #print(type(instruccion.ejecutar(controlador,ts)))
                sentencia = instruccion.ejecutar(controlador,tablaLocal)
                #print(ins)
                if isinstance(sentencia,SentenciaBreak):
                    #print("Se ha encontrado un break")
                    esBreak = True
                    break
