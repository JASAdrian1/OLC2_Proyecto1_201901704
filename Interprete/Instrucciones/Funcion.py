from Interprete.Interfaces.Instruccion import Instruccion


class Funcion(Instruccion):
    def __init__(self, id, listaParametros, listaInstrucciones, linea, columna):
        self.id = id
        self.listaParametros = listaParametros
        self.listaInstrucciones = listaInstrucciones
        self.linea = linea
        self.columna: columna