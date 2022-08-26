from random import randint

def jogo():
    entrada()
    dificuldade = difficulty()
    numero_sorte = randint(0,100)
    if (dificuldade == 1):
        vidas = 15
    elif(dificuldade == 2):
        vidas = 10
    elif(dificuldade == 3):
        vidas = 5
    while True:
        if(vidas == 0):
            print("VOCE PERDEU !!!")
            print("O numero era:", numero_sorte)
            print("\n")
            break
        chute = int(input("\nChute:"))
        if(chute > numero_sorte):
            vidas = vidas - 1
            if(chute > numero_sorte + 10):
                print("Chute muito alto, tente um mais baixo....")
                print("Vidas restantes:", vidas)
            else:
                print("Esta chegando perto, mas continua alto...")
                print("Vidas restantes:", vidas)
        elif(chute < numero_sorte):
            vidas = vidas - 1
            if(chute < numero_sorte - 10):
                print("Chute muito baixo, tente um mais alto...")
                print("Vidas restantes:", vidas)
            else:
                print("Esta chegando perto, mas continua baixo...")
                print("Vidas restantes:", vidas)
        else:
            print("Voce acertou!")
            break
    print("***********************")
    print("***** FIM DO JOGO *****")
    print("***********************")

def entrada():
    print("******************************")
    print("***** BEM VINDO AO JOGO! *****")
    print("******************************")

def difficulty():
    try:
        dificuldade = int(input("Digite a dificuldade desejada (1) facil, (2) medio (3) dificil:"))
    except Exception:
        print("Dificuldade inválida, tente de novo...\n")
        return entrada()
    return dificuldade

if(__name__ == "__main__"):
    jogo()