s="um tigre, dois tigres tres tigres"
p=0
while(p>-1):
    p=s.find("tigre",p)
    if p > 0:
        print("Posicao: %d" % p )
        p+=1
