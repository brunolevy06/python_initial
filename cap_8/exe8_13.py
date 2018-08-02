import random
n = random.randint(1,10)
y = 0
while y < 3:
    x = int(input("Escolha um número entre 1 e 10:"))
    if (x==n):
        print("Voce acertou")
    else:
        print("Voce errou")
    y+=1
