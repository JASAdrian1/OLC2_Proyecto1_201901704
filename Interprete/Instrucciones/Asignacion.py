from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.ast.nodo import Nodo


class Asignacion(Instruccion):
    def __init__(self, id, valor, linea, columna):
        self.id = id
        self.valor = valor
        self.linea = linea
        self.columna = columna
        self.tipoInstrucciones = "asignacion"

    def ejecutar(self, controlador, ts):
        variable = ts.getSimbolo(self.id)
        tipoNuevoValor = self.valor.getTipo(controlador, ts)
        if variable is not None:
            if variable.esMutable is True:
                if tipoNuevoValor == variable.tipoDato.tipo_enum:
                    variable.valor = self.valor.getValor(controlador, ts)
                    print(variable.valor)
                else:
                    print("***ERROR***El tipo de la variable no coincide con el nuevo valor agregrado")
            else:
                print("***ERROR***Se está intentado modificar una variable no mutable")
        else:
            print("***ERROR***La variable %s no ha sido declarada anteriormente" % self.id)


    def recorrer(self) -> Nodo:
        pass