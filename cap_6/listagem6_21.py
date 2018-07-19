ultimo = 10
fila = list(range(1,ultimo+1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual", fila)
    print("Digite F para adicionar um cliente ao final da fila,")
    print("Ou digite A para realizar o atendimento. S para sair")
    operacao = input("Operação (F, A ou S): ")
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print("Cliente %d atendido" % atendido)
        else:
            print("Fila vazia, ninguém para atender")
    elif operacao == "F":
        ultimo+=1 #Incrementando um cliente na fila
        fila.append(ultimo)
    
    elif operacao == "S":
        break
    else:
        print("Operacao invalida, digite F, A ou S")
