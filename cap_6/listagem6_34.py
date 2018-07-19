### Copie os valores pares para lista P e impares para a lista I

V=[9,8,7,12,0,13,21]
P=[]
I=[]
for e in V:
    if e % 2 ==0:
        P.append(e)
    else:
        I.append(e)
print("Pares: ", P)
print("Impares: ", I)
