notas=[6,7,5,8,9]
soma=0
contador=0

while contador < 5:
    soma += notas[contador]
    contador +=1
print("Media: %5.2f" % (soma/contador))
