from Interprete.Expresiones.InicializacionVector import InicializacionVector
from Interprete.Interfaces.Expresion import Expresion
from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.Error import Error
from Interprete.TablaSimbolos.Simbolo import Simbolo
from Interprete.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interprete.TablaSimbolos.Tipo import tipo


class LlamadaFuncion(Instruccion, Expresion):
    def __init__(self,id,parametros,linea,columna):
        self.id = id
        self.parametros = parametros
        self.linea = linea
        self.columna = columna
        self.tipoInstruccion = "llamadaFuncion"
        self.parametrosValidados = False

    def getTipo(self, controlador, ts) -> tipo:
        llamada = ts.getSimbolo(self.id)
        return llamada.tipoDato.tipo_enum

    def getValor(self, contralador, ts):
        if ts.verificarExisteGlobal(self.id):
            funcion = ts.getSimbolo(self.id)
            tablaLocal = TablaSimbolos(ts)
            if self.validarParametros(self.parametros,funcion.listaParametros,contralador,tablaLocal):
                self.parametrosValidados = True
                instruccion = funcion.ejecutar(contralador,tablaLocal)
                if instruccion != None:
                    return instruccion
        else:
            contralador.agregarAConsola(
                "***ERROR***Se ha llamado a una funcion no declarada")
            contralador.agregarError(
                Error("SEMANTICO", "Se ha llamado a una funcion no declarada", self.linea,
                      self.columna))


    def ejecutar(self, controlador, ts):
        for parametro in self.parametros:
            print("Parametro: ",parametro.expresion.getValor(controlador,ts))
            if isinstance(parametro.expresion.getValor(controlador,ts),InicializacionVector):
                print(parametro.expresion.getValor(controlador,ts).expresion)
        funcion = ts.getSimbolo(self.id)
        tablaLocal = TablaSimbolos(ts)
        if funcion is not None:
            if self.parametros is not None:
                if self.parametrosValidados == False:
                    if self.validarParametros(self.parametros,funcion.listaParametros,controlador,tablaLocal):
                        #self.parametrosValidados = True
                        instruccion = funcion.ejecutar(controlador, tablaLocal)
                        if instruccion != None:
                            return instruccion
                    else:
                        print("Ha ocurrido un error en la llamada de la funcion")
                else:
                    print("Ha ocurrido un error en la llamada de la funcion")
                    self.parametrosValidados = True
                    instruccion = funcion.ejecutar(controlador, tablaLocal)
                    if instruccion != None:
                        return instruccion
            else:
                if self.parametros is None and funcion.listaParametros is None:
                    instruccion = funcion.ejecutar(controlador, tablaLocal)
                    if instruccion != None:
                        return instruccion
                else:
                    controlador.agregarAConsola(
                        "***ERROR***La cantidad de parametros en la llamada no conincided con la declarada en la funcion")
                    controlador.agregarError(
                        Error("SEMANTICO", "La cantidad de parametros en la llamada no conincided con la declarada en la funcion", self.linea,
                              self.columna))
        else:
            controlador.agregarAConsola(
                "***ERROR***Se ha llamado a una funcion que no ha sido declarada")
            controlador.agregarError(
                Error("SEMANTICO",
                      "La funcion que se ha llamado no ha sido de declarada",
                      self.linea,
                      self.columna))




    def validarParametros(self, parametrosLlamada, parametrosFuncion, controlador, ts):         #parametroFuncion es tipo Parametro()
        if len(parametrosFuncion) == len(parametrosLlamada):                                    #parametroLlamada es tipo Expresion()
            for i in range(0,len(parametrosFuncion)):
                auxiliarFuncion = parametrosFuncion[i]
                auxiliarIdFuncion = auxiliarFuncion.id
                auxiliarTipoFuncion = auxiliarFuncion.tipo.tipo_enum

                auxiliarLlamada = parametrosLlamada[i]
                print("Expresion parametro: ",auxiliarLlamada.expresion)
                auxiliarTipoLlamada = auxiliarLlamada.expresion.getTipo(controlador,ts)
                auxiliarValorLlamada = auxiliarLlamada.expresion.getValor(controlador,ts)
                print("VALIDACION DE PARAMETROS: ",auxiliarTipoLlamada, " == ", auxiliarTipoFuncion)
                if auxiliarTipoLlamada == auxiliarTipoFuncion:
                    print("Parametro agregado a la tabla de simbolos")
                    print("ID = ",auxiliarIdFuncion)
                    print("Valor = ",auxiliarValorLlamada)
                    #if auxiliarFuncion.esPorReferencia == True:    ***AGREGAR VALIDACION ACA PARA QUE SEAN POR VALOR O POR REFERENCIA LOS PARAMETROS
                    nuevoSimbolo = Simbolo(auxiliarIdFuncion,auxiliarValorLlamada,"variable",
                                           auxiliarFuncion.tipo,"",auxiliarFuncion.esMutable,auxiliarFuncion.linea,auxiliarFuncion.columna)
                    ts.agregarSimbolo(auxiliarFuncion.id,nuevoSimbolo)
                else:
                    print("NO SE HA AGREGADO EL PARAMETRO A LA TABLA DE SIMBOLOS :C")
                    print(auxiliarLlamada.expresion.getValor(controlador, ts))
            return True
        else:
            controlador.agregarAConsola(
                "***ERROR***Error en la validacion de los parametros")
            controlador.agregarError(
                Error("SEMANTICO", "Error en la validacion de los parametros", self.linea,
                      self.columna))


