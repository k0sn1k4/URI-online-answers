#include <stdio.h>
int main(){
    int n1, hora, minutos;
    scanf("%d", &n1);
    hora = n1 / 3600;
    n1 = n1 - hora*3600;
    minutos = n1 / 60;
    if(minutos >= 60){
        n1 = (n1 - minutos*60);}
    else{
        n1 = (n1 - minutos * 60);}
    printf("%i:%i:%i\n", hora,minutos,n1);
}