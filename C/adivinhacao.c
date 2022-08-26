#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

    int NumeroSecreto, chute;
    int segundos = time(0);
    srand(segundos);
    int numerogrande = rand();

    NumeroSecreto = numerogrande % 1000;

    printf("***************************************\n");
    printf("** Bem vindo ao jogo de adivinhação! **\n");
    printf("***************************************");

    while(chute != NumeroSecreto){

        printf("\nQual é o seu chute? ");
        scanf("%d", &chute);
        if(chute == NumeroSecreto){
            printf("\nParabéns, você ACERTOU o número secreto!\n");
        }
        else{
            if(chute > NumeroSecreto){
                printf("Seu chute foi muito alto, tente de novo...\n");
            }
            else{
                printf("Seu chute foi muito baixo, tente de novo...\n");
            }
            
        }
    }

    return 0;

}