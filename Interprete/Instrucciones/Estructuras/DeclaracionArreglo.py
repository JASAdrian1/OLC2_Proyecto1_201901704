from Interprete.Interfaces.Instruccion import Instruccion
from Interprete.TablaSimbolos.Error import Error
from Interprete.TablaSimbolos.Simbolo import Simbolo, lista_simbolos


class DeclaracionArreglo(Instruccion):
    def __init__(self, id, valor, tipo, tipoElementos, estructuraArreglo, esMutable, linea, columna):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.tipoElementos = tipoElementos
        self.estructuraArreglo = estructuraArreglo
        self.esMutable = esMutable
        self.linea = linea
        self.columna = columna

    #FALTA LA VALIDACION DE DATOS DEL ARREGLO
    def ejecutar(self, controlador, ts):
        print("Se esta declarando un arreglo")
        #print(self.tipoElementos.tipo_enum)
        #print(self.estructuraArreglo)
        #print(self.valor)
        #print(self.tipo)
        #self.validarTiposElementos(controlador,ts)
        for id in self.id:
            if ts.verificarActualExiste(id):
                print("***ERROR***El id \"%s\" ya ha sido declarado anteriormente" % id)
                controlador.agregarError(
                    Error("SEMANTICO", "El id \"%s\" ya ha sido declarado anteriormente" % id, self.linea,
                          self.columna))
                controlador.agregarAConsola("***ERROR***El id \"%s\" ya ha sido declarado anteriormente" % id)
            else:
                if self.valor is not None:
                    if self.tipoElementos is not None:
                        print(self.tipoElementos.tipo_enum, "   (impreso desde declaracion array)")
                        nuevo_simbolo = Simbolo(self.id,self.valor,"arreglo",self.tipo,"",self.esMutable,
                                                self.linea, self.columna,
                                                tipoElementosArray=self.tipoElementos.tipo_enum,estructuraArr=self.estructuraArreglo)
                        lista_simbolos.append(nuevo_simbolo)
                        ts.agregarSimbolo(id, nuevo_simbolo)
                        pass
                    else:
                        tipoElementos = self.getElementoBasico(self.valor)  #Se guarda un valor del arreglo
                        print(tipoElementos.tipo.tipo_enum,"   (impreso desde declaracion array)")
                        nuevo_simbolo = Simbolo(self.id, self.valor, "arreglo", self.tipo, "", self.esMutable, self.linea,
                                                self.columna,
                                                tipoElementosArray=tipoElementos.tipo.tipo_enum, estructuraArr=self.estructuraArreglo)
                        lista_simbolos.append(nuevo_simbolo)
                        ts.agregarSimbolo(id, nuevo_simbolo)
                else:
                    print("NO SE HA AGREGADO VALORES AL ARREGLO, SE DEBERIA DE PERMITIR?")

    def validarTiposElementos(self, controlador, ts):
        longitudes_dimensiones = self.estructuraArreglo[1:]
        print(self.valor[0][0][2].getValor(controlador,ts))
        for longitud in longitudes_dimensiones:
            for i in range(0,longitud):
                print("Hola")
                #print(self.valor[i].getValor(controlador, ts))

    def recorrerArreglo(self,arreglo, cantidadDimensiones, dimensionAcual):
        if dimensionAcual > 1:
            return self.recorrerArreglo(arreglo,dimensionAcual+1)
        else:
            return arreglo

    def getElementoBasico(self,expresion):
        if isinstance(expresion,list):
            return self.getElementoBasico(expresion[0])
        else:
            return expresion
