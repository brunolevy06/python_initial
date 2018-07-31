

### Função que recebe uma lista e duas outras funções como parâmetros
### Para cada elemento na lista L, se a condição for satisfeita, chamamos a a função impressão.
def imprime_lista(L, fimpressão, fcondição):
     for e in L:
         if fcondição(e):
               fimpressão(e)

### Função que imprime o elemento da lista
def imprime_elemento(e):
     print("Valor: %d" % e)

### Funcao que verifica se o numero é par
def épar(x):
     return x % 2 == 0

### Funcao que verifica se o numero é impar
def éimpar(x):
     return not épar(x)

### Passamos a lista
L = [1,7,9,2,11,0]
imprime_lista(L, imprime_elemento, épar)
imprime_lista(L, imprime_elemento, éimpar)
