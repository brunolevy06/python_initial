def triangulo(base,altura):
    area = (base * altura)/2
    return area

base = int(input("Digite a base do triangulo: "))
altura = int(input("Digite a altura do triangulo: "))

print(triangulo(base,altura))
