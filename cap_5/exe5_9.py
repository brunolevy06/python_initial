### Escreva um programa que leia dois numeros. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisao de dois numeros como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20% 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

x = 0
while num1 >= num2:
	num1 = num1 - num2
	x = x + 1

print("O resultado da divisao é: %i e o resto é: %i" % (x, num1))
