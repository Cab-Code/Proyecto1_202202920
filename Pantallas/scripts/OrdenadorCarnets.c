#include <stdio.h>
#include <stdlib.h>

int carnets[10];

void crearLista(char carnetStr[], int i){
    int carnet = (int) strtol(carnetStr, NULL, 10);
    carnets[i] = carnet;
}

void quickSort(int carnets[], int inicio, int fin){
    int i, f, piv, aux;
    i = inicio;
    f = fin;
    piv = carnets[(i + f)/2];

    do{
        while(carnets[i] < piv && i < fin){
            i++;
        }
        while(carnets[f] > piv && f > inicio){
            f--;
        }
        if(i <= f){
            aux = carnets[i];
            carnets[i] = carnets[f];
            carnets[f] = aux;
            i++;
            f--; 
        }
    }while(i <= f);

    if(inicio <= f){
        quickSort(carnets, inicio, f);
    }
    if(fin > i){
        quickSort(carnets, i, fin);
    }
}

void imprimir(int carnets[], int tam){

    for (int i = 0; i < tam; i++)
    {
        printf("%d\n", carnets[i]);
    }
    
}

int main () { 
FILE *archivo;
char caracter;
char lectura[10];
int tamano = 0;
int i = 0;
archivo = fopen("carnetsprueba.txt", "r");
if (archivo != NULL){
    while (feof(archivo) == 0){ 
            fgets (lectura, 10, archivo); 
            crearLista(lectura, i);
            i++;
        }
    fclose(archivo); 
}else{
    printf("Error al abrir el archivo. \n");
    printf("El archivo no existe o no se tienen permisos de lectura. \n");
}

tamano = i;

printf("Tamano: %d", tamano);

quickSort(carnets, 0, i);
printf(carnets);
imprimir(carnets, i);
}