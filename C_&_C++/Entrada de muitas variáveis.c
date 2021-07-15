#include <stdio.h>

int main()
{   
    float dividendo, divisor;
    
    printf("Digite dois numeros reais: ");
    scanf("%f %f", &dividendo, &divisor);
    printf("O resultao da divisão entre %.2f e %.2f vale %.2f", dividendo, divisor, dividendo/divisor);
}
