import random
from arbol import Arbol

arbol_numeros = Arbol(76476)
for i in range(1000000):
    arbol_numeros.agregar(random.randint(-10000000, 10000000))
    

arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()