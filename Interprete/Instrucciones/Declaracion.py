from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.Tipo import tipo, Tipo
from Interprete.ast.nodo import Nodo
from Interprete.TablaSimbolos.Simbolo import lista_simbolos
from Interprete.TablaSimbolos.Simbolo import Simbolo


class Declaracion(Instruccion):
    def __init__(self, tipo, valor, lista_id,esMutable, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.lista_id = lista_id
        self.esMutable = esMutable
        self.fila = fila
        self.columna = columna
        self.tipoInstruccion = "declaracion"

    def ejecutar(self, controlador, ts):
        for id in self.lista_id:
            if ts.verificarActualExiste(id):
                print("***ERROR***El id \"%s\" ya ha sido declarado anteriormente" % id)
            else:
                if self.valor is not None:
                    if self.tipo is not None:
                        if self.tipo.tipo_enum == self.valor.getTipo(controlador,ts):
                            nueva_variable = Simbolo(id,self.valor.getValor(controlador,ts),"variable",self.tipo,"", self.esMutable,self.fila,self.columna)
                            lista_simbolos.append(nueva_variable)
                            ts.agregarSimbolo(id,nueva_variable)
                    else:
                        tipo_new_varible = tipo(self.valor.getTipo(controlador,ts)).name    #Se obtiene el string del nombre del valor en el enum
                        tipo_new_varible = Tipo(tipo_new_varible)       #Con el nombre obtenido se crea un objeto de tipo Tipo
                        nueva_variable = Simbolo(id, self.valor.getValor(controlador, ts), "variable", tipo_new_varible, "",
                                                 self.esMutable, self.fila, self.columna)
                        lista_simbolos.append(nueva_variable)
                        #print("++++",nueva_variable.tipoDato)
                        ts.agregarSimbolo(id, nueva_variable)



    def recorrer(self) -> Nodo:
        pass