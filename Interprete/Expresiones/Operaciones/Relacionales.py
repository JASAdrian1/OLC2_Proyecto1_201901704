from Interprete.Expresiones.Operacion import Operacion, operador
from Interprete.TablaSimbolos.Tipo import tipo
from Interprete.ast.nodo import Nodo


class Relacionales(Operacion):
    def __init__(self, exp1, exp2, expU, linea, col, signo):
        super(Relacionales, self).__init__(exp1, exp2, expU, linea, col, signo)


    def getTipo(self, controlador, ts) -> tipo:
        tipo_expresion1 = self.exp1.getTipo(controlador, ts)
        tipo_expresion2 = self.exp2.getTipo(controlador, ts)
        if tipo_expresion1 == tipo.ERROR or tipo_expresion2 == tipo.ERROR:
            print("***ERROR***Error con algun tipo de los operadores de la operacion relacional")
            return tipo.ERROR
        if (tipo_expresion1 == tipo_expresion2) and (tipo_expresion1 == tipo.I64 or tipo_expresion1 == tipo.F64 or tipo_expresion1 == tipo.STRING):
            return tipo.BOOL
        else:
            controlador.agregarAConsola("***ERROR***Los operadores de laa operacion relacional no coinciden %s != %s\n" % (tipo_expresion1, tipo_expresion2))
            return tipo.ERROR




    def getValor(self, controlador, ts):
        tipo_expresion1 = self.exp1.getTipo(controlador, ts)
        tipo_expresion2 = self.exp2.getTipo(controlador, ts)
        valor_expresion1 = self.exp1.getValor(controlador, ts)
        valor_expresion2 = self.exp2.getValor(controlador, ts)
        if (tipo_expresion1 and tipo_expresion2) != tipo.ERROR:
            if tipo_expresion1 == tipo_expresion2:
                if self.operador_enum == operador.MAYORQUE:
                    return valor_expresion1 > valor_expresion2
                if self.operador_enum == operador.MAYORIGUAL:
                    return valor_expresion1 >= valor_expresion2
                if self.operador_enum == operador.MENORQUE:
                    return valor_expresion1 < valor_expresion2
                if self.operador_enum == operador.MENORIGUAL:
                    return valor_expresion1 <= valor_expresion2
                if self.operador_enum == operador.IGUALACION:
                    print(valor_expresion1, " == ",valor_expresion2)
                    #print(valor_expresion1 == valor_expresion2,"asddasdasdasd")
                    return  valor_expresion1 == valor_expresion2
                if self.operador_enum == operador.DISTINTO:
                    return valor_expresion1 != valor_expresion2
            else:
                print("***ERROR***La comparaciona no se esta realizando entre valores del mismo tipo")
        else:
            print("***ERROR***Existe algun problema con alguno de los operadores de la operaicon relacional")
        return None




    def recorrer(self) -> Nodo:
        pass