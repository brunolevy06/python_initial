def multiple(a,b):
    if a % b == 0:
        return True
    else:
        return False

a = int(input("digite um numero: "))
b = int(input("digite um numero: "))

print(multiple(a,b))
