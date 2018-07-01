### Escreva um programa que leia dois numeros. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois numeros como somas sucessivas de um deles. Assim, 5 x 4 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

x = 1

# X recebe o valor de 1, mas enquanto for menor do que o num1, o while será true e contiuará executando.
while x < num1:
    num2 = num2 + num2
    x = x + 1 

print(num2) 
