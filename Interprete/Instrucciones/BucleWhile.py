from Interprete.Instrucciones.SentenciaBreak import SentenciaBreak
from Interprete.TablaSimbolos.Error import Error
from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interprete.TablaSimbolos.Tipo import tipo


class BucleWhile(Instruccion):
    def __init__(self, expresion, instrucciones, linea, columna):
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna
        self.tipoInstruccion = "while"


    def ejecutar(self, controlador, ts):
        esBreak = False
        anteriosEsCiclo = controlador.esCiclo
        condicion = self.expresion.getValor(controlador, ts)
        tipoCondicion = self.expresion.getTipo(controlador,ts)
        if tipoCondicion == tipo.BOOL:
            while condicion == True and esBreak == False:
                tablaLocal = TablaSimbolos(ts)
                for instruccion in self.instrucciones:
                    sentencia = instruccion.ejecutar(controlador, tablaLocal)
                    if isinstance(sentencia,SentenciaBreak):
                        controlador.esCiclo = anteriosEsCiclo
                        return sentencia
                condicion = self.expresion.getValor(controlador, ts)    #Se verifica si la condicion del while se sigue cumpliendo
        else:
            controlador.agregarAConsola("***ERROR***La condicion del bucle while no es de tipo booleano")
            controlador.agregarError(Error("SEMANTICO","La condicion del bucle while no es de tipo booleano",self.linea,self.columna))
