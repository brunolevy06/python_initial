### Um programa que controal a utilização das salas de um cinema. Imagine que a lista Salas = [10,2,1,3,0] contenha o mumero de lugares vagos nas salas 1,2,3,4 e 5 respectivamente. Esse programa lerá o número da sala e a quantidade de lugares solicitados. ELe deve informar se é possível vender o numero de lugares solicitados, ou seja, se ainda há lugares livres. Caso seja possível vender os bilhetes, atualizará o numero de lugares livres. A saída occrre quando se digita 0 no numero da sala.

lugares_vagos=[10,2,1,3,0]
while True:
    sala=int(input("Sala (0 sai): "))
 
    if sala == 0:
        print("Fim")
        break
 
    if sala > len(lugares_vagos) or sala<1:
        print("Sala invalida")
   
    elif lugares_vagos[sala-1]==0:
        print("Sala Lotada")
   
    else:
        lugares = int(input("Quantos lugares voce deseja (%d vagos): " % lugares_vagos[sala-1]))
   
        if lugares > lugares_vagos[sala-1]:
            print("Esse numero de lugares nao esta disponivel.")
   
        elif lugares < 0:
            print("Numero invalido")
   
        else:
            lugares_vagos[sala-1]-=lugares
            print("%d lugares vendidos" % lugares)

print("Utilização das salas")
for x,l in enumerate(lugares_vagos):
    print("Sala %d - %d lugares vazios" % (x+1,l))
