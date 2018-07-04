### Escreva um program qye leia numeros inteiros do teclado. O programa deve ler os numeros ate que o usuario digite 0 (zero). No final da execução exiba a quantidade de números digitados, assim como a soma e a média aritimética.

soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número para somar ou 0 para sair: "))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1

print("Quantidade de numeros digitados: ", quantidade)
print("Soma dos numeros digitados: ", soma)
print("Media dos numeros digitados: ", (soma/quantidade))
        

