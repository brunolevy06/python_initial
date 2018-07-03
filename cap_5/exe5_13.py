### Escreva um programa que pergunte o valor inicial de uma divida e o juros mensal. Pergunte tamém o valor mensal que será pago. IMprima o número de meses para que a divida seja paga, total pago e o total de juros.

divida = float(input("Digite o valor da divida "))
monthpay = float(input("Qual valor pretende pagar mensalmente? "))
taxa = float(input("Qual o juros mensal dessa dívida? "))

mes = 1

if (divida * (taxa/100) > monthpay):
    print("Sua dívida não será paga nunca, pois os juros são maiores do que o pagamento mensal")
else:
    saldo = divida
    juros_paid = 0
    while saldo > monthpay:
        juros = saldo * (taxa/100)
        saldo = saldo + juros - monthpay
        juros_paid = juros_paid + juros
        print("Até agora os juros pagos sao %6.2f" % juros_paid)
        print("Seu saldo da divida no mes %d é de %6.2f " % (mes,saldo))
        mes = mes + 1
    print ("Para pagar uma dívida de R$%8.2f, a %5.2f %% de juros," % (divida, taxa))
    print ("você precisará de %d meses, pagando um total de R$%8.2f de juros." % (mes-1, juros_paid))
    print ("No último mês, você teria um saldo residual de R$%8.2f a pagar." % (saldo))  
