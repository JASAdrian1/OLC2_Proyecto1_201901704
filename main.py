

from Analizador.gramatica import analizar_entrada

f = open("./entrada.txt", "r")
input = f.read()
analizar_entrada(input)