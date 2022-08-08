import enum
from Interprete.Interfaces.Expresion import Expresion
from Interprete.TablaSimbolos.Tipo import Tipo, tipo
from Interprete.ast.nodo import Nodo


class Operacion(Expresion):

    def __init__(self, exp1, exp2, expU, linea, col, signo):
        self.exp1 = exp1
        self.exp2 = exp2
        self.expU = expU
        self.operador = signo
        self.linea = linea
        self.col = col
        self.signo = signo

    def getOperador(self,signo):
        return tipo_operacion.get(signo)


    def getTipo(self, controlador, ts) -> tipo:
        pass

    def getValor(self, contralador, ts):
        pass

    def recorrer(self) -> Nodo:
        pass


class operador(enum.Enum):
    SUMA = 0
    RESTA = 1
    MULT = 2
    DIV = 3
    POT = 4
    MOD = 5
    MAYORQUE = 6
    MENORQUE = 7
    MAYORIGUAL = 8
    MENORIGUAL = 9
    IGUALACION = 10
    DISTINTO = 11
    OR = 12
    AND = 13
    NOT = 14
    UNARIO = 15


tipo_operacion = {
    '+': operador.SUMA,
    '-': operador.RESTA,
    '/': operador.DIV,
    '*': operador.MULT,
    '%': operador.MOD,
    '^': operador.POT,
    '>=': operador.MAYORIGUAL,
    '>': operador.MAYORQUE,
    '<=': operador.MENORIGUAL,
    '<': operador.MENORQUE,
    '==': operador.IGUALACION,
    '!=': operador.DISTINTO,
    '||': operador.OR,
    '&&': operador.AND,
    '!': operador.NOT,
    'UNARIO': operador.UNARIO
}