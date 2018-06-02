# encoding: utf-8

vel = int(input("Digite a velocidade do carro em km/h: "))

if vel > 80:
    multa = (vel - 80) * 5
    print("Voce foi multado em %4.2f" % multa)
     
