sequencia = input("Digite a string: ")

contador = {}

for letra in sequencia:
    if letra in contador:
        contador[letra]+=1
    else:
        contador[letra]=1

for chave in contador:
    print("%s: %dx" % (chave, contador[chave] )  )
