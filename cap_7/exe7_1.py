a=input("Digite a primeira string: ")
b=input("Digite a segunda string: ")

p=a.find(b)
if p >=0:
    print("A string \"%s\" esta contida na string \"%s\", mais precisamente na posicao %d"% (b,a,p))
else:
    print("A string \"%s\" nao esta contida na string \"%s\")" % (b,a)) 
