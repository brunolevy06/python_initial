salario = int(input("Digite seu salario: "))

if salario > 1250:
    aumento = salario * 0.1
    total = salario + aumento
    print("com o aumento de %d, seu salario vai ficar %d reais" % (aumento, total))
else:
    aumento = salario * 0.15
    total = salario + aumento
    print("com o aumento de %d, seu salario vai ficar %d reais" % (aumento, total))
