### Funcao recebe uma lista L, inicia um contador e em cada ítem da lista adicionamos seu valor ao contador de nome total
def soma(L):
     total = 0
     for e in L:
         total += e
     return total

### Na função "média" pegamos o resultado da funcao "soma" e dividimos pela quantidade de ítens da lista L para obtermos a média
def media(L):
     return( soma(L) / len(L) )
