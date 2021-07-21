#include <stdio.h>

int main (){
    int opcao;
    
    printf("Entre com um número inteiro: \n");
    scanf("%d", &opcao);

    if (opcao > 0){
        
        if ((opcao%2) == 0){
            printf("\nNúmero positivo e Par!\n");
        }
        else{
            printf("\nNúmero positivo e Ímpar!\n");
        }
    }    
    else if (opcao == 0){
        printf("\nNúmero nulo.\n");
        printf("\nNúmero negativo!\n");    
    }
    else{
        printf("\nNúmero negativo!\n");
    }   
}
