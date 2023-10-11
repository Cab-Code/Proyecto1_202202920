#include <stdio.h>
#include <stdlib.h>

int carnets[100];

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
       /* printf("%d\n", carnets[i]);
       */
    }
}

void escribir(int carnets[], int tam){
    FILE *archivo;
    int i = 0;
    archivo = fopen("Pantallas/carnets.txt", "w");
    char carnet[100];
    if (carnet != 0){
        for(i = 1; i < tam; i++){
            sprintf(carnet, "%d\n", carnets[i]);
            fputs(carnet, archivo);
    }
    sprintf(carnet, "%d", carnets[i]);
    fputs(carnet, archivo);
    }
    

    fclose(archivo); 
}

int main () { 
FILE *archivo;
char caracter;
char lectura[100];
int i = 0;
archivo = fopen("Pantallas/carnets.txt", "r");
if (archivo != NULL){
    while (feof(archivo) == 0){ 
            fgets (lectura, 100, archivo); 
            crearLista(lectura, i);
            i++;
        }
    fclose(archivo); 
}else{
    printf("Error al abrir el archivo. \n");
    printf("El archivo no existe o no se tienen permisos de lectura. \n");
}


quickSort(carnets, 0, i);
imprimir(carnets, i);
escribir(carnets, i);

return 0;
}