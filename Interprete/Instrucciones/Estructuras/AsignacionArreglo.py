from Interprete.Interfaces.Instruccion import Instruccion


class AsignacionArreglo(Instruccion):
    def __init__(self, id, acceso, expresion, fila, columna):
        self.id = id
        self.acceso = acceso
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def ejecutar(self, controlador, ts):
        print("Se esta asignando un nuevo valor al arreglo")
        variable = ts.getSimbolo(self.id)
        tipoNuevoValor = self.expresion.getTipo(controlador, ts)
        if variable is not None:
            if variable.esMutable is True:
                if variable.tipoDato == "VEC":          # POR LA FORMA EN QUE SE ALMACENAN LOS VECTORES Y LOS ARREGLOS
                    lista = variable.valor.expresion    # CUANDO SE ACCEDE A UN VECTOR ES NECESARIO ACCEDER A UN ATRIBUTO
                else:                                   # ADICICONAL
                    lista = variable.valor
                #print("Variable lista: ",variable.valor)
                posicionesAcceso = self.acceso  # Arreglo con las posiciones que se quiere ingresar al arreglo en las distintas dimensiones
                if len(posicionesAcceso) > 1:
                    for i in range(0,len(posicionesAcceso)-1):
                        lista = lista[posicionesAcceso[i].getValor(controlador, ts)]
                    posicionAcceso = posicionesAcceso[len(posicionesAcceso) - 1]
                    print(lista)
                else:
                    posicionAcceso = self.acceso[0]
                if tipoNuevoValor == lista[posicionAcceso.getValor(controlador, ts)].getTipo(controlador, ts):
                    lista[posicionAcceso.getValor(controlador, ts)].valor = self.expresion.valor
