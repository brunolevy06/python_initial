### Escreva um programa para controlar uma pequena máquina registradora. Voce deve solicitar ao usuário que digite o código do produto e a quantidade comprada.

# O Acumulador pagamento recebe o valor 0
pagamento = 0

### Vamos primeiro checar se o código digitado pelo usuário é válido ou se ele quer finalizar a compra
### Usamos o if elif para isso, acredito que daria para usar lista ou algo do tipo, mas nesse inicio preferimos fazer a forma mais simples.

while True:
    codigo = int(input("Digite o codigo do produto: " ))
    preco = 0
    if codigo == 0:
        break;
    elif codigo == 1:
        preco = 0.50
    elif codigo == 1:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Codigo invalido")

### Após checarmos se o código é válido, passamos para o próximo passo.
### Checamos se preco é diferente de zero, ou seja, se foi digitado um codigo válido, caso a resposta seja positiva, aí sim pedimos a quantidade de determinado produto e começamos a jogar os valores no acumulador "pagamento". Esse processo se repetirá até que o usuário digite 0 e o programa saia de dentro do while.

    if preco != 0:
        quantidade = int(input("Digite a quantidade de produtos que deseja: "))
        pagamento = pagamento + (preco * quantidade)

### É impresso o valor total das compras
print("O total será R$%6.2f" % pagamento)
         
