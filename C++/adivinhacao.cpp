#include <iostream>
using namespace std;

int main(){

    cout << "***********************" << endl;
    cout << "** Bem vindo ao Jogo **" << endl;
    cout << "***********************" << endl;

    int numero_secreto = 42;
    cout << "O número secreto é: " << numero_secreto << endl;

    bool nao_acertou = true;
    int tentativas = 0;

    while(nao_acertou){
        int chute;

        tentativas++;

        cout << "Tentativa número: " << tentativas << endl;
        cout << "Qual o seu chute? ";
        cin >> chute;

        bool acertou = chute == numero_secreto;
        bool maior = chute > numero_secreto;

        if(acertou){
            cout << "Parabéns, você acertou o número secreto!" << endl;
            nao_acertou = false;
        }

        else if(maior){
            cout << "Seu chute foi maior que o número secreto..." << endl;
        }

        else{
            cout << "Seu chute foi menor que o número secreto..." << endl;
        }
    }
    
}