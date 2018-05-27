#encoding: utf-8

dias = int(input("Digite o numero de dias: "))
horas = int(input("Digite o numero de horas: "))
minutos = int(input("Digite o numero de minutos: "))
segundos = int(input("Digite o numero de segundos: "))

total = ((dias * 86400) + (horas * 3600) + (minutos * 60) + segundos)

print(total)
