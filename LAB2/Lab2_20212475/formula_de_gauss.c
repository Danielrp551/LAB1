#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


//; nasm -f elf64 asmFloatInnerProd.asm -o asmFloatInnerProd.o
// gcc asmFloatInnerProd.o floatInnerProd.c -o floatInnerProd -lm
// ./floatInnerProd

extern float asmCalcularAreaPoligono(float *x,float *y,int N);
float  cCalcularAreaPoligono(float *x,float *y,int N);

int main(){

    float * x, * y;
    int N = 6;
    x = malloc(N*sizeof(float));
    y = malloc(N*sizeof(float));
    double cArea, asmArea;

    //Lectura
    for(int i = 0; i < N; i++){
        scanf("%f", &x[i]);
        scanf("%f", &y[i]);       
    }
    struct timespec ti, tf;
    double elapsed, tC, tAsm;
     
    clock_gettime(CLOCK_REALTIME, &ti);
    cArea =cCalcularAreaPoligono(x,y,N);
    clock_gettime(CLOCK_REALTIME, &tf);
    tC = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    //tC = tf.tv_nsec-ti.tv_nsec;
    printf("El area calculada en C es : %.3f\n",cArea);
    printf("El tiempo de ejecuccion en C es : %.2f ns\n",tC);
    
    
    clock_gettime(CLOCK_REALTIME, &ti);
    asmArea = asmCalcularAreaPoligono(x,y,N);
    clock_gettime(CLOCK_REALTIME, &tf);
    tAsm = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    //tAsm = tf.tv_nsec-ti.tv_nsec;
    printf("El area calculada en ASM es: %.3f\n", asmArea);
    printf("El tiempo de ejecuccion en ASM es : %.2f ns\n",tAsm);
    
    printf("\n");
    double SpeedUp = (tC)/(tAsm);

    printf("El SpeedUp entre C y ASM es: %.3f\n",SpeedUp);

    return 0;
}

float  cCalcularAreaPoligono(float *x,float *y,int N){
    float suma1=0, suma2=0;
    for(int i=0; i<N-1; i++){
        suma1 += x[i]*y[i+1];
        suma2 += x[i+1]*y[i];       
    } 
    suma1-= suma2;
    suma1+= x[N-1]*y[0];
    suma1-= x[0]*y[N-1];
    return 0.5*(fabs(suma1));
}