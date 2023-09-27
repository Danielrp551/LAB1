#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


//; nasm -f elf64 asmFloatInnerProd.asm -o asmFloatInnerProd.o
// gcc asmFloatInnerProd.o floatInnerProd.c -o floatInnerProd -lm
// ./floatInnerProd

extern void AsmavgFilter(float *x,int N,float *y);
void CavgFilter(float *x,int N,float *y);

int main(){
    int N;

    N = 10;

    float *x, *y;
    x = malloc(N*sizeof(float));
    y = malloc(N*sizeof(float));

    x[0] = 3;
    x[1] = 9;
    x[2] = 4;
    x[3] = 52;
    x[4] = 3;
    x[5] = 8;
    x[6] = 6;
    x[7] = 2;
    x[8] = 2;
    x[9] = 9;


    struct timespec ti, tf;
    double elapsed, tC, tAsm;
    
    clock_gettime(CLOCK_REALTIME, &ti);
    CavgFilter(x,N,y);
    clock_gettime(CLOCK_REALTIME, &tf);
    tC = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    //tC = tf.tv_nsec-ti.tv_nsec;
    printf("Tiemplo de ejecuccion en nanosegundos en C : %f\n",tC);
    for(int i=0; i<N;i++)
        printf("%f  ",y[i]);
    printf("\n");
    
    clock_gettime(CLOCK_REALTIME, &ti);
    AsmavgFilter(x,N,y);
    clock_gettime(CLOCK_REALTIME, &tf);
    tAsm = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    //tAsm = tf.tv_nsec-ti.tv_nsec;
    printf("Tiemplo de ejecuccion en nanosegundos en Asm : %f\n",tAsm);
    for(int i=0; i<N;i++)
        printf("%f  ",y[i]);
    printf("\n");
    double SpeedUp = (tC)/(tAsm);

    printf("El SpeedUp entre C y ASM es: %f\n",SpeedUp);

    return 0;
}

void CavgFilter(float *x,int N,float *y){
    double nMenos1, n, nMas1;
    for(int i=0; i<N;i++){
        if(i==0){
            nMenos1 = x[i];
            n = x[i];
            nMas1 = x[i+1];
        }
        if(i==N-1){
            nMenos1 = x[i-1];
            n = x[i];
            nMas1 = x[i];   
        }
        if(i!= 0 && i!= N-1){
            nMenos1 = x[i-1];
            n = x[i];
            nMas1 = x[i+1];      
        } 
        y[i] = (nMenos1+n+nMas1)/3;
    }
}

