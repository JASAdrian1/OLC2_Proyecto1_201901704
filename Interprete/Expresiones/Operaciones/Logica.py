from Interprete.Expresiones.Operacion import Operacion, operador
from Interprete.TablaSimbolos.Tipo import tipo
from Interprete.ast.nodo import Nodo


class Logica(Operacion):
    def __init__(self,exp1, exp2, expU, linea, col, signo):
        super(Logica, self).__init__(exp1, exp2, expU, linea, col, signo)


    def getTipo(self, controlador, ts) -> tipo:
        if self.expU == False:
            tipo_expresion1 = self.exp1.getTipo(controlador, ts)
            tipo_expresion2 = self.exp2.getTipo(controlador, ts)
            if tipo_expresion1 == tipo.BOOL and tipo_expresion2 == tipo.BOOL:
                return tipo.BOOL
            else:
                print("***ERROR***Alguno de los operadores de la operacion logica no es de tipo booleano")
        else:
            tipo_expresion1 = self.exp1.getTipo(controlador, ts)
            if tipo_expresion1 == tipo.BOOL:
                return tipo.BOOL
            else:
                print("***ERROR***EL operador de la operacion logica no es de tipo booleano")
                return tipo.ERROR


    def getValor(self, contralador, ts):
        if self.expU == False:
            tipo_expresion1 = self.exp1.getTipo(contralador, ts)
            tipo_expresion2 = self.exp2.getTipo(contralador, ts)
            valor_expresion1 = self.exp1.getValor(contralador, ts)
            valor_expresion2 = self.exp2.getValor(contralador, ts)
        else:
            tipo_expresion1 = self.exp1.getTipo(contralador, ts)
            valor_expresion1 = self.exp1.getValor(contralador, ts)
            if tipo_expresion1 == tipo.BOOL:
                return not valor_expresion1
            else:
                print("***ERROR***EL operador de la operacion logica no es de tipo booleano")
                return None
        if tipo_expresion1 == tipo.BOOL and tipo_expresion2 == tipo.BOOL:
            if valor_expresion1 == "false":
                val_bool_exp1 = False
            else:
                val_bool_exp1 = True
            if valor_expresion2 == "false":
                val_bool_exp2 = False
            else:
                val_bool_exp2 = True
            if self.operador_enum == operador.OR:
                return val_bool_exp1 or val_bool_exp2
            elif self.operador_enum == operador.AND:
                return val_bool_exp1 and val_bool_exp2
        else:
            print("***ERROR***Alguno de los operadores de la operacion logica no es de tipo booleano")
            return None

    def recorrer(self) -> Nodo:
        pass
