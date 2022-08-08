from Interprete.Expresiones.Operacion import Operacion, operador
from Interprete.TablaSimbolos.Tipo import Tipo, tipo, validar_tipo
from Interprete.ast.nodo import Nodo


class Aritmetica(Operacion):

    def __init__(self, exp1, exp2, expU, linea, col, signo):
        super(Aritmetica, self).__init__(exp1, exp2, expU, linea, col, signo)

    def getTipo(self, controlador, ts) -> tipo:
        if self.expU == False:
            tipo_exp1 = self.exp1.getTipo(controlador,ts)
            tipo_exp2 = self.exp2.getTipo(controlador, ts)
            print(tipo_exp2)
            print(tipo_exp1)
            if tipo_exp1 == tipo.ERROR or tipo_exp2 == tipo.ERROR:
                return tipo.ERROR
        else:
            tipo_exp1 = self.exp1.getTipo(controlador, ts)
            if tipo_exp1 == tipo.ERROR:
                return  tipo.ERROR
        print(self.operador)
        resultado = validar_tipo.get(self.operador, tipo.ERROR)
        if resultado == tipo.ERROR:
            print("c")
            return tipo.ERROR
        resultado2 = resultado.get(tipo_exp1,tipo.ERROR)
        if resultado2 == tipo.ERROR:
            return tipo.ERROR
        return resultado2.get(tipo_exp2, tipo.ERROR)


    def getValor(self, contralador, ts):

        if self.expU == False:
            tipo_exp1 = self.exp1.getTipo(contralador, ts)
            tipo_exp2 = self.exp2.getTipo(contralador, ts)
            valor_exp1 = self.exp1.getValor(contralador, ts)
            valor_exp2 = self.exp2.getValor(contralador, ts)
        else:
            tipo_expu = self.exp1.getTipo(contralador, ts)
            tipo_exp1 = tipo.ERROR
            tipo_exp2 = tipo.ERROR

        if tipo_exp1 != tipo.ERROR and tipo_exp2 != tipo.ERROR:
            if self.operador == operador.SUMA:
                if tipo_exp1 == tipo.I64 or tipo_exp1 == tipo.F64:
                    return valor_exp1 + valor_exp2
                else:
                    return None


    def recorrer(self) -> Nodo:
        pass
