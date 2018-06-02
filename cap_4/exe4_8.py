numa = int(input("Digite um numero: "))
numb = int(input("Digite um numero: "))

operacao = raw_input("Digite a operacao: (soma, subtracao, divisao, multiplicacao) : ")

if operacao == "soma":
    print(numa + numb)

elif operacao == "divisao":
    print(numa / numb)

elif operacao == "multiplicacao":
    print(numa * numb)

elif operacao == "subtracao":
    print(numa - numb)

else:
    print("Voce nao escolheu uma operacao valida")

