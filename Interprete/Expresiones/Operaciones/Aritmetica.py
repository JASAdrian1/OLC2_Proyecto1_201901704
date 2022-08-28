from Interprete.Expresiones.Operacion import Operacion, operador
from Interprete.TablaSimbolos.Tipo import Tipo, tipo, validar_tipo
from Interprete.ast.nodo import Nodo


class Aritmetica(Operacion):

    def __init__(self, exp1, exp2, expU, linea, col, signo):
        super(Aritmetica, self).__init__(exp1, exp2, expU, linea, col, signo)

    def getTipo(self, controlador, ts) -> tipo:
        if self.expU == False:      #Si no es unario se busca el tipo de las dos expresiones de la operacion
            #print(self.exp1.getValor, "      ",self.exp2)
            tipo_exp1 = self.exp1.getTipo(controlador,ts)
            tipo_exp2 = self.exp2.getTipo(controlador, ts)
            #print(tipo_exp2)
            #print(tipo_exp1)
            if tipo_exp1 == tipo.ERROR or tipo_exp2 == tipo.ERROR:
                print("b")
                return tipo.ERROR
        else:                                                   #Si es unario se busca el tipo del unico valor
            tipo_exp1 = self.exp1.getTipo(controlador, ts)
            if tipo_exp1 == tipo.ERROR:
                return  tipo.ERROR
            print(tipo_exp1)
            return tipo_exp1
        print(self.operador_enum)
        resultado = validar_tipo.get(self.signo, tipo.ERROR)
        if resultado == tipo.ERROR:
            print("c")
            return tipo.ERROR
        resultado2 = resultado.get(tipo_exp1,tipo.ERROR)
        if resultado2 == tipo.ERROR:
            print("a")
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
            valor_expu = self.exp1.getValor(contralador,ts)
            tipo_exp1 = tipo.ERROR
            tipo_exp2 = tipo.ERROR
            if tipo_expu == tipo.I64 or tipo_expu == tipo.F64:
                return -valor_expu

        if tipo_exp1 != tipo.ERROR and tipo_exp2 != tipo.ERROR:
            if tipo_exp1 == tipo_exp2:
                if self.operador_enum == operador.SUMA:
                    if tipo_exp1 == tipo.I64 or tipo_exp1 == tipo.F64:
                        return valor_exp1 + valor_exp2
                    else:
                        print("***ERROR*** Tipo de dato invalido para realizar suma")
                        return None
                if self.operador_enum == operador.RESTA:
                    if tipo_exp1 == tipo.I64 or tipo_exp1 == tipo.F64:
                        return valor_exp1 - valor_exp2
                    else:
                        print("***ERROR*** Tipo de dato invalido para realizar resta")
                        return  None
                if self.operador_enum == operador.MULT:
                    if tipo_exp1 == tipo.I64 or tipo_exp1 == tipo.F64:
                        return valor_exp1 * valor_exp2
                    else:
                        print("***ERROR*** Tipo de dato invalido para realizar multiplicacion")
                        return None
                if self.operador_enum == operador.DIV:
                    if tipo_exp1 == tipo.I64 or tipo_exp1 == tipo.F64:
                        return valor_exp1 / valor_exp2
                    else:
                        print("***ERROR*** Tipo de dato invalido para realizar division")
                        return None
                if self.operador_enum == operador.MOD:
                    if tipo_exp1 == tipo.I64 or tipo_exp2 == tipo.F64:
                        return valor_exp1 % valor_exp2
                    else:
                        print("***ERROR*** Tipo de dato invalido para realizar modulo")
                        return None
                if self.operador_enum == operador.POT:
                    if tipo_exp1 == tipo.I64:
                        return pow(valor_exp1,valor_exp2)
                    else:
                        print("***ERROR*** Tipo de dato invalido para realizar potencia de enteros")
                        return None
                if self.operador_enum == operador.POTF:
                    if tipo_exp1 == tipo.F64:
                        return pow(valor_exp1, valor_exp2)
                    else:
                        print("***ERROR*** Tipo de dato invalido para realizar potencia de flotantes")
                        return None
            else:
                print("***ERROR***. Los tipos de los dos operadores en la operacion artimetica no coinciden")
                return None
        else:
            print("***ERROR*** Verificar el tipo de alguno de los dos operadores de la operacion aritmetica")
            return None


    def recorrer(self) -> Nodo:
        pass
