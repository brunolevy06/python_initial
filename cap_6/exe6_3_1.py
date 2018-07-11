### Faça um programa que leia duas listas e que gere uma terceira com os elemtnos das duas primeiras, sem elementos repetidos

primeira = []
segunda = []

while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar): "))
    if e == 0:
        break
    primeira.append(e)

while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar): "))
    if e == 0:
        break
    segunda.append(e)

terceira = []

### Adicionar todos os elementos da lista "primeira" na lista "terceira" 
x = 0
while x < len(primeira): 
    terceira.append(primeira[x])
    x+=1
x = 0


### Checa se os elementos da segunda lista estão na terceira
while x < len(segunda):
        if segunda[x] not in terceira:
            terceira.append(segunda[x])
        x+=1

print(terceira)
