km = input("Digite a quantidade de km percorridos: ")
dias = input("Digite a quantidade de dias que o carro ficou alugado: ")

aluguel_dia = 60.00
aluguel_km = 0.15 

total = (aluguel_dia * dias) + (km * aluguel_km)

print("O valor total eh %4.2f" % total)
