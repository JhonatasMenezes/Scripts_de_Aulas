#include <stdio.h>

int main (){
    int opcao;
    
    printf("Entre com um número inteiro: \n");
    scanf("%d", &opcao);

    if (opcao > 0){
        printf("\nNúmero positivo!\n");
    }    
    else if (opcao == 0){
        printf("\nNúmero nulo.\n");
        printf("\nNúmero negativo!\n");    
    }
    else{
        printf("\nNúmero negativo!\n");
    }
    
}
