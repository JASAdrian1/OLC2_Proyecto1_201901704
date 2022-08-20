from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.Error import Error
from Interprete.ast.nodo import Nodo
from Interprete.TablaSimbolos.Tipo import tipo
from Interprete.TablaSimbolos.TablaSimbolos import TablaSimbolos


class SentenciaIf(Instruccion):
    def __init__(self,condicion, instruccionesIf, instruccionesElse, linea, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.linea = linea
        self.columna = columna


    def ejecutar(self, controlador, ts):
        if self.condicion.getTipo(controlador, ts) == tipo.BOOL:
            if self.condicion.getValor(controlador, ts) == True:
                for instruccion in self.instruccionesIf:
                    tablaLocal = TablaSimbolos(ts)
                    instruccion.ejecutar(controlador, tablaLocal)
            else:
                if self.instruccionesElse is not None:
                    for instruccion in self.instruccionesElse:
                        tablaLocal = TablaSimbolos(ts)
                        instruccion.ejecutar(controlador, tablaLocal)
        else:
            controlador.agregarAConsola("***ERROR***La condicion de la sentencia if no es de tipo booleano")
            controlador.agregarError(
                Error("SEMANTICO", "La condicion de la sentencia if no es de tipo booleano", self.linea,
                      self.columna))

    def recorrer(self) -> Nodo:
        pass