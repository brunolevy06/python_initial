### Escreva um programa que pergunte o depósito inicial, o deposito mensal  e a taxa de juros de uma poupança. Exiba os valores mes a mes para os 24 primeiros meses. Escreva o total ganho com juros no período.


deposito = int(input("Digite o valor do deposito inicial: " ))
investimento = int(input("Digite o valor investimento mensal: " ))
juros = float(input("Digite o valor dos juros (em porcentagem) mensais: " ))

mes = 1
saldo = deposito 

while mes <= 24:
    saldo = saldo + (saldo * (juros/100)) + investimento 
    print("O valor do mes %d foi %4.2f" % (mes, saldo) )  
    mes = mes + 1 
