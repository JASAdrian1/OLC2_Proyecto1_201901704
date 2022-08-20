

class TablaSimbolos:
    def __init__(self, tabAnterior):
        self.tablaAnterior = tabAnterior
        self.tabla = {}

    def agregarSimbolo(self, id, simbolo):
        id = id.lower()
        self.tabla[id] = simbolo

    def verificarExisteGlobal(self,id):
        ts = self
        while ts is not None:
            if id.lower() in ts.tabla:
                return True
            ts = ts.tablaAnterior
        return False

    def verificarActualExiste(self, id):
        if id in self.tabla:
            return True
        else:
            return False

    def getSimbolo(self, id):
        ts = self
        while ts is not None:
            if id.lower() in ts.tabla:
                return ts.tabla[id.lower()]
            ts = ts.tablaAnterior
        return None