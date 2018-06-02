consumo = float(input("Digite seu consumo em kWh: "))
instalacao = raw_input("Qual o tipo de instalacao? (Residencial = r, industrial = i ou comercial = c)? ")

if instalacao == "r":
	if consumo <= 500:
		total = consumo * 0.40
		print("O valor a pagar eh %2.2f " % total)
        else:
		total = consumo * 0.65
		print("O valor a pagar eh %2.2f " % total)

	
if instalacao == "c":
	if consumo <= 1000:
		total = consumo * 0.55
		print("O valor a pagar eh %2.2f " % total)
        else:
		total = consumo * 0.60
		print("O valor a pagar eh %2.2f " % total)

if instalacao == "i":
	if consumo <= 500:
		total = consumo * 0.55
		print("O valor a pagar eh %2.2f " % total)
        else:
		total = consumo * 0.60
		print("O valor a pagar eh %2.2f " % total)
