from Interprete.Instrucciones.SentenciaBreak import SentenciaBreak
from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.Error import Error
from Interprete.TablaSimbolos.TablaSimbolos import TablaSimbolos


class Funcion(Instruccion):
    def __init__(self, id, tipo, listaParametros, listaInstrucciones, linea, columna):
        self.id = id
        self.tipo = tipo
        self.listaParametros = listaParametros
        self.listaInstrucciones = listaInstrucciones
        self.linea = linea
        self.columna = columna
        self.tipoInstruccion = "funcion"

    def ejecutar(self, controlador, ts):
        tablaLocal = TablaSimbolos(ts)
        for instruccion in self.listaInstrucciones:
            sentencia = instruccion.ejecutar(controlador,tablaLocal)
            if isinstance(sentencia,SentenciaBreak):
                return sentencia
        return None


    def agregarFuncion(self,controlador, ts):
        if ts.verificarExisteGlobal(self.id):
           controlador.agregarAConsola("***ERROR***La funcion ya ha sido declarada anteriormente")
           controlador.agregarError(Error("Semantico","La funcion ya ha sido declarada anteriormente",self.linea,self.columna))
        else:
            ts.agregarSimbolo(self.id,self)
            print("Se ha agregado la funcion a la tabla de simbolos")
