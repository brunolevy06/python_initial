mercadoria = int(input("Digite o preco da mercadoria: "))
desconto = float(input("Digite quantos por cento sera o desconto: "))

v_desconto = (desconto / 100) * mercadoria
v_mercadoria = mercadoria - v_desconto

print("O valor da mercadoria ficou %4.2f, pois o valor do desconto foi %4.2f" % (v_mercadoria, v_desconto) )
