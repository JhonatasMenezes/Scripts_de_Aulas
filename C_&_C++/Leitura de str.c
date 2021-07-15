#include <stdio.h>

void main()
{   
    char ch1, ch2;
    
    printf("Digite duas letras: ");
    scanf("%c ", &ch1);
    fflush(stdin);
    scanf("%c", &ch2);
    printf("As letras digitadas foram %c e %c", ch1, ch2);
}
