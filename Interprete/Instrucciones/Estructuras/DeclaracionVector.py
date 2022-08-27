from Interprete.Expresiones.InicializacionVector import InicializacionVector
from Interprete.Expresiones.Primitivo import Primitivo
from Interprete.Interfaces.Expresion import Expresion
from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.Error import Error
from Interprete.TablaSimbolos.Simbolo import Simbolo, lista_simbolos
from Interprete.TablaSimbolos.Tipo import Tipo
from Interprete.TablaSimbolos.Tipo import tipo


class DeclaracionVector(Instruccion):
    def __init__(self,id,expresion,tipo,tipoElementos,esMutable,withCapacity,linea,columna):
        self.id = id
        self.expresion = expresion
        self.tipo = tipo
        self.tipoElementos = tipoElementos
        self.esMutable = esMutable
        self.withCapacity = withCapacity
        self.linea = linea
        self.columna = columna


    def ejecutar(self, controlador, ts):
        print("Se esta declarando el vector")
        for id in self.id:
            if ts.verificarActualExiste(id):
                print("***ERROR***El id \"%s\" ya ha sido declarado anteriormente" % id)
                controlador.agregarError(Error("SEMANTICO","El id \"%s\" ya ha sido declarado anteriormente" % id,self.linea,self.columna))
                controlador.agregarAConsola("***ERROR***El id \"%s\" ya ha sido declarado anteriormente" % id)
            else:
                if self.withCapacity is None:
                    if self.expresion is not None:
                        print(self.expresion)
                        if self.expresion.repeticiones == 0:
                            print(self.expresion.repeticiones,"***************-***")
                            if self.tipoElementos is None:      #Si no se indica de que tipo son los elementos desde la declaracion se debe encontrar el tipo
                                elementoBasico = self.getElementoBasico(self.expresion)
                                tipoElementos = elementoBasico.getTipo(controlador,ts)
                            else:                               #Si ya indica el tipo en la declaracion unicamente se copia el valor
                                tipoElementos = self.tipoElementos
                            nuevoSimbolo = Simbolo(id,self.expresion,"vector",self.tipo,"",self.esMutable,self.linea,self.columna,
                                                   tipoElementosArray=tipoElementos,estructuraArr=self.expresion)
                            print(elementoBasico,"*-*-*-*-*-*-*-")
                            print(tipoElementos, "*-*-*-*-*-*-*-")
                            lista_simbolos.append(nuevoSimbolo)
                            ts.agregarSimbolo(id, nuevoSimbolo)
                else:
                    self.rellenarVecWithCapacity(controlador,ts)
                    #print(self.expresion)


    def getElementoBasico(self,expresion):
        if isinstance(expresion,InicializacionVector):
            return self.getElementoBasico(expresion.expresion[0])
        else:
            return expresion

    def rellenarVecWithCapacity(self,controlador,ts):
        valor = self.determinarValorDefecto(self.tipoElementos)
        self.expresion = []
        if isinstance(self.withCapacity,Expresion):
            for i in range(0,self.withCapacity.getValor(controlador,ts)):
                #print(self.tipoElementos.tipo_enum)
                #print(self.tipoElementos)
                self.expresion.append(InicializacionVector(Primitivo(valor,self.tipoElementos.tipo,self.linea,self.columna),0))
        else:
            self.expresion.append(None)
            print("HOLAAAAAAAAAAAAAAAA")

    def determinarValorDefecto(self,tipoElemento):
        if tipoElemento.tipo_enum == tipo.I64:
            valor = 0
        elif tipoElemento.tipo_enum == tipo.F64:
            valor = 0.0
        elif tipoElemento.tipo_enum == tipo.STR:
            valor = ""
        elif tipoElemento.tipo_enum == tipo.BOOL:
            valor = False
        else:
            valor = None
        return valor