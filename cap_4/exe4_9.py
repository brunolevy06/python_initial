valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salario? "))
anos = int(input("Em quantos anos pretende pagar? "))

meses = anos * 12
prestacao = valor_casa / meses

custo_maximo = 0.3 * salario

if prestacao < custo_maximo:
	print("Parabens! Realizaremos o emprestimo pois sua prestacao de %4.2f eh menor do que 30 por cento do seu salario %4.2f" % (prestacao,salario))
else:
	print("Seu emprestimo nao foi aprovado =( ")

