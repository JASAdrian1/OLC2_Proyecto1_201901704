
class Simbolo:
    def __init__(self, id, valor, tipoVarFun, tipoDato, entorno, esMutable, linea, columna, listaParametros = None, metodo = None):
        self.id = id
        self.tipoVarFun = tipoVarFun
        self.tipoDato = tipoDato
        self.entorno = entorno
        self.esMutable = esMutable
        self.linea = linea
        self.columna = columna
        self.valor = valor
        self.listaParametros = listaParametros
        self.metodo = metodo



lista_simbolos = []