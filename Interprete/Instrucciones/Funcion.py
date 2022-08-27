from Interprete.Instrucciones.SentenciaBreak import SentenciaBreak
from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.TablaSimbolos import TablaSimbolos


class Funcion(Instruccion):
    def __init__(self, id, tipo, listaParametros, listaInstrucciones, linea, columna):
        self.id = id
        self.tipo = tipo
        self.listaParametros = listaParametros
        self.listaInstrucciones = listaInstrucciones
        self.linea = linea
        self.columna: columna

    def ejecutar(self, controlador, ts):
        tablaLocal = TablaSimbolos(ts)
        for instruccion in self.listaInstrucciones:
            sentencia = instruccion.ejecutar(controlador,tablaLocal)
            if isinstance(sentencia,SentenciaBreak):
                return sentencia
        return None