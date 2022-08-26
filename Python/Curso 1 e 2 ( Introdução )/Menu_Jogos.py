import forca
import adivinhacao

def menu():
    print("*****************")
    print("*** Bem vindo ***")
    print("*****************\n")
    try:
        jogo = int(input("Qual jogo deseja jogar? (1) forca (2) adivinhação:"))
    except Exception:
        print("Opção inválida...")
    if(jogo == 1):
        forca.jogo()
    elif(jogo == 2):
        adivinhacao.jogo()
if(__name__ == "__main__"):
    menu()

