from Interprete.Interfaces.Expresion import Expresion
from Interprete.TablaSimbolos.Error import Error
from Interprete.TablaSimbolos.Tipo import tipo
from Interprete.ast.nodo import Nodo


class AccesoVector(Expresion):
    def __init__(self,id,accesoArreglo,linea,columna):
        self.id = id
        self.accesoArreglo = accesoArreglo
        self.linea = linea
        self.columna = columna


    def getValor(self, contralador, ts):
        print("OBTNIENDO VALOR DEL ACCESO AL ARREGLO")
        arreglo = ts.getSimbolo(self.id)        #Se obtiene el arreglo con el id especificado de la tabla de datos
        if arreglo is not None:
            valoresAcceso = []
            for acceso in self.accesoArreglo:
                valoresAcceso.append(acceso.getValor(contralador,ts))      #Se guardan los valores en un arreglo
                                                                           #con valores de las posiciones a
                                                                           #las que se quiere acceder en el vector
            valoresLimites = arreglo.estructuraArr[1:]     #Se guarda en un arreglo los valores de las dimensiones que posee el arreglo
                                                           #Se quita el primer elemento ya que contiene el tipo de datos de los elementos del arreglo
            valoresLimites.reverse()    #Se invierten los valores, ya que estos se encuentran almacenados al reves
            seExcedeLimit = False
            #print(valoresLimites,"-*-*-*-")
            #print(valoresAcceso, "-/-/-/-")
            for i in range(0,len(valoresLimites)):
                if i >= len(valoresAcceso):         #Se deja de verificar cuando el arreglo posea mas dimensiones que el acceso
                    break
                if valoresAcceso[i] >= valoresLimites[i] or valoresAcceso[i] < 0:   #Se verifica que el acceso al vector no sobrepase el limite
                    seExcedeLimit = True

            if seExcedeLimit == False:
                valorRetornar = arreglo.valor
                #print(valorRetornar,"++++++6+")
                for dimension in valoresAcceso:
                    valorRetornar = valorRetornar[dimension]
                #print(valorRetornar,"-.-.-.-.-.-.")
                return valorRetornar.getValor(contralador,ts)
            else:
                contralador.agregarAConsola("***ERROR***Se esta intentando accerder afuera de los limites del arreglo")
                contralador.agregarError(
                    Error("SEMANTICO", "Se esta intentando accerder afuera de los limites del arreglo", self.linea,
                          self.columna))
        else:
            contralador.agregarAConsola("***ERROR***El arreglo al que se esta accediendo no exite")
            contralador.agregarError(
                Error("SEMANTICO", "El arreglo al que se esta accediendo no exite", self.linea,
                      self.columna))



    def getTipo(self, controlador, ts) -> tipo:
        arreglo = ts.getSimbolo(self.id)
        #print("Tipo: ",arreglo.tipoElementosArray.tipo_enum)
        return arreglo.tipoElementosArray

    def recorrer(self) -> Nodo:
        pass