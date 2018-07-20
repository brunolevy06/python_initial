string1=input("Digite a primeira string: ")
string2=input("Digite a segunda string: ")
string3=[]

for y in string2:
    if y in string1:
        string3.append(y)

s="".join(string3)
if len(s) > 1:
    print(s)
else:
    print("Nenhuma letra faz parte")
