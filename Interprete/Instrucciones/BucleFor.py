from Interprete.Instrucciones.Asignacion import Asignacion
from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.Instrucciones.RecorridoFor import RecorridoFor
from Interprete.TablaSimbolos.Simbolo import Simbolo
from Interprete.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interprete.TablaSimbolos.Tipo import tipo, Tipo


class BucleFor(Instruccion):
    def __init__(self,recorrido,instrucciones,linea,columna):
        self.recorrido = recorrido
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna


    def ejecutar(self, controlador, ts):
        variableControl = self.recorrido
        if self.recorrido.inicio is not None and self.recorrido.fin is not None:
            tablaPrevia = TablaSimbolos(ts)
            tipo_new_varible = tipo(variableControl.inicio.getTipo(controlador, ts)).name
            tipo_new_varible = Tipo(tipo_new_varible)
            #print("TIPO:   ",tipo_new_varible.tipo)
            nuevoSimbolo = Simbolo(variableControl.id,variableControl.inicio.getValor(controlador,ts),
                                   "variable",tipo_new_varible,"",True,self.linea,self.columna)
            tablaPrevia.agregarSimbolo(variableControl.id,nuevoSimbolo)
            #A traves de la variable actualizacion se determina si el ciclo se recorrer de forma ascendente o descendente
            if variableControl.inicio.getValor(controlador,ts) < variableControl.fin.getValor(controlador,ts):
                actualizacion = 1
            elif variableControl.inicio.getValor(controlador,ts) > variableControl.fin.getValor(controlador,ts):
                actualizacion = -1
            variableRecorrido = tablaPrevia.getSimbolo(variableControl.id)
            limiteEmergencia = 0
            while variableRecorrido.valor  != variableControl.fin.getValor(controlador,ts):
                tablaLocal = TablaSimbolos(tablaPrevia)                                 #Se crea una nueva tabla local para el for
                for instruccion in self.instrucciones:                                  #Se ejecutan las instrucciones dentro del for
                    instruccion.ejecutar(controlador,tablaLocal)
                variableRecorrido.valor = variableRecorrido.valor + actualizacion       #Se acutaliza la variable que se esta recorriendo en el rango
                limiteEmergencia+=1
                if limiteEmergencia == 300:
                    print("Se ha salido del for de emergencia")
                    break
        else:
            tablaPrevia = TablaSimbolos(ts)
            listaARecorrer = None
            if type(self.recorrido.objetoARecorrer) is not list:
                lista = tablaPrevia.getSimbolo(self.recorrido.objetoARecorrer.id)
                if lista is not None:
                    if lista.tipoDato == "VEC":
                        print(lista.valor.expresion)
                        print(lista.tipoDato)
                        elementoInicial = lista.valor.expresion[0]
                        listaARecorrer = lista.valor.expresion
                    elif lista.tipoDato == "ARRAY":
                        print(lista.valor)
                        elementoInicial = lista.valor[0]
                        listaARecorrer = lista.valor
                else:
                    print("Se encontro la lista??????????????")
            else:
                lista = self.recorrido.objetoARecorrer
                elementoInicial = lista[0]
                listaARecorrer = lista
                # print(lista.valor.expresion)
                # print(lista.tipoDato)
            nuevoSimbolo = Simbolo(variableControl.id, elementoInicial.getValor(controlador, ts),
                                   "variable", elementoInicial.getTipo(controlador, ts), "", True,
                                   self.linea, self.columna)
            tablaPrevia.agregarSimbolo(variableControl.id, nuevoSimbolo)

            if listaARecorrer is not None:
                variableRecorrido = tablaPrevia.getSimbolo(variableControl.id)
                for elemento in listaARecorrer:
                    tablaLocal = TablaSimbolos(tablaPrevia)
                    variableRecorrido.valor = elemento.getValor(controlador,ts)
                    for instruccion in self.instrucciones:
                        instruccion.ejecutar(controlador,tablaLocal)



