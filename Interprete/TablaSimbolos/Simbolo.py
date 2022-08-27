
class Simbolo:
    def __init__(self, id, valor, tipoVarFun, tipoDato, entorno, esMutable, linea,
                 columna, tipoElementosArray=None, estructuraArr=None, listaParametros = None, metodo = None):
        self.id = id
        self.tipoVarFun = tipoVarFun
        self.tipoDato = tipoDato
        self.entorno = entorno
        self.esMutable = esMutable
        self.linea = linea
        self.columna = columna
        self.valor = valor
        self.tipoElementosArray = tipoElementosArray
        self.estructuraArr = estructuraArr
        self.listaParametros = listaParametros
        self.metodo = metodo



lista_simbolos = []