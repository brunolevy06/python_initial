primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ""

for letra in primeira:
    if letra not in segunda:
        terceira += letra


if terceira == "":
    print("Todos os caracteres foram removidos.")
else:
    print("Os caracteres %s foram removidos de %s, gerando: %s" % (segunda, primeira, terceira))
