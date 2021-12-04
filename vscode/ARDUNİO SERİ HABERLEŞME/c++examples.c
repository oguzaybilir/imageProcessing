/*Karar 1*/
#include <stdio.h>
#include <conio.h>
int main(void){
	int a;
	printf("Bir tamsayi giriniz:"); scanf("%d",&a);
	if(a>0) printf("Pozitif");
	else if(a<0) printf("Negatif");
	else printf("Sifir");
	getch();
	return 0;
}