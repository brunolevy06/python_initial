#encoding: utf-8

salario = int(input("Digite quanto e seu salario: "))
aumento = float(input("Digite de quantos por cento sera seu aumento: "))

valor_aumento = (aumento / 100) * salario
total = salario + valor_aumento

print("O salario final ficara no valor de %4.2f, pois o aumento sera de %4.2f" % (total,valor_aumento))






