from random import randint

def jogo():
    entrada()
    palavra_secreta = carrega_palavra().upper()
    vidas = dificuldade()
    palavra = []
    tentativas = []
    for j in range(len(palavra_secreta) - 1):
        palavra.append('_')
    print("\nPalavra secreta -> ",palavra)
    while True:
        achou = False
        repetida = False
        chute = input("\nChute:").upper()
        if (chute in tentativas):
            print("Voce ja tentou essa letra, tente outra...")
            repetida = True
        else:
            tentativas.append(chute)
        i = 0
        for aux in range(len(palavra_secreta) - 1):
            if(chute == palavra_secreta[i]):
                palavra[i] = chute
                achou = True
            i = i + 1
        print("chutes ->", tentativas)
        print("Palavra secreta -> ",palavra)
        if '_' not in palavra:
            print("************************")
            print("**** VOCE GANHOU!!! ****")
            print("************************")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
            break
        if (vidas == 0):
            print("**************************")
            print("***** VOCE PERDEU!!! *****")
            print("**************************")
            print("    _______________         ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\  ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ")
            print("")
            print("A palavra era:", palavra_secreta)
            break
        if(achou == False and repetida == False):
            vidas = vidas - 1
            print("Errou, restam {} vidas".format(vidas))

def dificuldade():
    difficulty = int(input("\nSelecione a dificuldade (1)facil (2)moderado (3)dificil:"))
    if(difficulty == 1):
        vidas = 15
    elif(difficulty == 2):
        vidas = 10
    elif(difficulty == 3):
        vidas = 5
    else:
        print("Opção inválida, tente de novo...")
        return dificuldade()
    return vidas

def carrega_palavra():
    i = 0
    arq = open("palavras.txt", "r")
    aux = randint(1,195)
    for escolha in arq:
        i = i + 1
        if(i == aux):
            escolhida = escolha
    return escolhida

def entrada():
    print("*********************")
    print("*** Jogo da Forca ***")
    print("*********************")

if(__name__ == "__main__"):
    jogo()