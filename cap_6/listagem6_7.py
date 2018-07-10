numeros=[0,0,0,0,0]
x = 0
while x < 5:
    numeros[x]=int(input("Numero %d: " % (x + 1)))
    x += 1
while True:
    escolhido=int(input("Que posição voce quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print("Você escolheu o numero: %d" % (numeros[escolhido-1]))
