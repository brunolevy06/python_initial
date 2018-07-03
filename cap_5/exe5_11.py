### Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mes a mes para os 24 primeiros meses. Escreva o total ganho com juros no período.


deposito = int(input("Digite o valor do deposito inicial: " ))
juros = float(input("Digite o valor dos juros (em porcentagem) mensais: " ))

mes = 1
saldo = deposito 

while mes <= 24:
    saldo = saldo + (saldo * (juros/100))
    print("O valor do mes %d foi %4.2f" % (mes, saldo) )  
    mes = mes + 1 
