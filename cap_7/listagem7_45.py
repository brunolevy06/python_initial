### Variavale palavra recebe a palavra secreta, tudo minusculo e sem espaços no final e no inicio.
palavra = input("Digite a palavra secreta:").lower().strip()

### Esse for é para que pulemos várias linhas para que a palavra secreta não apareça para o jogador
for x in range(100):
     print()

### Listas para receber as letras digitadas e os acertos
digitadas = []
acertos = []

### Contador para a quantidade de erros
erros = 0
while True:
     senha = ""

### Como a lista "acertos" está vazia, na primeira passagem por esse for, senha vai ser composta apenas por pontos.
### Ex: palavra = levy, senha = ....

     for letra in palavra:
         senha += letra if letra in acertos else "." ### Incrementa letra, se letra estiver em acertos, senão incrementa o .
     print(senha)

### No momento que senha for igual a palavra, o jogo acaba e temos um break
     if senha == palavra:
         print("Você acertou!")
         break

### Aqui começa o jogo em si, é esperado que o usuário digite uma letra, vamos garantir que nao tenha espaços, esteja tudo lower e vamos armazená-la na variável "tentativa".
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas: ### Verificamos se a letra já foi digitada antes, se sim, avisamos ao usuário, continuamos para o else
         print("Você já tentou esta letra!")
         continue ### Deve-se ignorar todas as linhas até o final da repeção e voltar para o início, sem terminá-la, isso faz com que o programa volte para o While.
     else:
         digitadas += tentativa ### A lista "digitadas" recebe a letra digitada.
         if tentativa in palavra: ### Se a letra digitada fizer parte da palavra, adicionamos a tentativa na lista de acertos.
               acertos += tentativa
         else:
               erros += 1 ### Se a tentativa nao fizer parte da palavra, incrementamos a variável erros e avisamos ao usuario.
               print("Você errou!")
     print("X==:==\nX  :   ")
     print("X  :  ")
     print("X  O   " if erros >= 1 else "X")
     linha2 = ""
     if erros == 2:
         linha2 = "  |   "
     elif erros == 3:
         linha2 = " \|   "
     elif erros >= 4:
         linha2 = " \|/ "
     print("X%s" % linha2)
     linha3 = ""
     if erros == 5:
         linha3 += " /     "
     elif erros >= 6:
         linha3 += " / \ "
     print("X%s" % linha3)
     print("X\n===========")
     if erros == 6:
         print("Enforcado!")
         break
