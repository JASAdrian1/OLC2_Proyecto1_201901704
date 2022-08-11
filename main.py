

from Analizador.gramatica import analizar_entrada
from Interprete.Controlador import Controlador
from Interprete.TablaSimbolos.TablaSimbolos import TablaSimbolos

controlador = Controlador()
ts = TablaSimbolos()

f = open("./entrada.txt", "r")
input = f.read()
nodos = analizar_entrada(input)
for nodo in nodos:
    print("---------------------------------------------------")
    #print(nodo)
    print(nodo.getTipo(controlador,ts))
    print(nodo.getValor(controlador,ts))