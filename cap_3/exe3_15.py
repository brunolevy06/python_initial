cpd = input("Digite a quantidade de cigarros por dia: ")
anos = input("Tem fumado por quantos anos? ")

tcigarros = (anos * 365) * cpd

dias_perdidos = ((tcigarros * 10) / (60 * 24))

print("O numero de dias perdidos foi %d" % dias_perdidos)
