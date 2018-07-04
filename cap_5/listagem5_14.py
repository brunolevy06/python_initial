## Um programa que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor. Para simplificar vamos trabalhar apenas com valores inteiros e com cedulas de 50, 20, 10, 5 e 1

## Primeiro momento, pedimos o valor a pagar
## Definimos que o valor de celulas é 0
## A variavel atual recebe o numero da cedula de maior valor disponível, no caso, 50.
## A variavel apagar recebe o valor definido pelo usuario na entrada.
valor=int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor


## No while, vamos checar se o valor a pagar é maior do que a cedula de maior valor, se a resposta for positiva, retiramos o valor de ATUAL do valor APAGAR e adicionamos a quatidade de cedulas no CONTADOR cedulas.
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
## Caso o valor a pagar seja menor do que a cedula de maior valor, entramos no else, onde imprimimos o número de CEDULAS com o valorde ATUAL que já foram usadas.
## Após a impressão dos valores, utilizamos os valores subsequentes, do maior para o menor (20,10,5 e 1) e o colocamos na variável ATUAL e reiniciamos a checagem (se o valor APAGAR é maior do que a variável ATUAL). Fazemos essa checagem até que o valor APAGAR seja0.
## No final do else zeramos o contador de CEDULAS, para que só seja incrementado caso algum dos valores do if e elifs sejam menores do que o valor APAGAR
    else:
        print("%d cedulas de R$%d" % (cedulas, atual))
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
