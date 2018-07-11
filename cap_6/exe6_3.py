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

##
terceira = []

duas_listas = primeira[:] 
duas_listas.extend(segunda)

x=0
while x < len(duas_listas):
   y = 0
   while y < len(terceira):
        if duas_listas[x] == terceira[y]:
            break
        y=y+1
   if y == len(terceira):
        terceira.append(duas_listas[x])
   x=x+1
x=0
while x < len(terceira):
    print("%d: %d" % (x,terceira[x]))
    x=x+1  
