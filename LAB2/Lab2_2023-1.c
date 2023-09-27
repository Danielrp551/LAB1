
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


//; nasm -f elf64 asmFloatInnerProd.asm -o asmFloatInnerProd.o
// gcc asmFloatInnerProd.o floatInnerProd.c -o floatInnerProd -lm
// ./floatInnerProd

extern void asmCalcularDistancias(float *longitud,float* latitud,int N,float * ciudades);
void cCalcularDistancias(float *longitud,float *latitud,int N,float *ciudades);

int main(){

    float *ciudades, *longitud, *latitud;
    int N = 5;
    ciudades =  malloc(N * sizeof(float));  
    longitud =  malloc(N * sizeof(float));  
    latitud =  malloc(N * sizeof(float));  

    longitud[0] = 15.3;
    longitud[1] = 13.1;
    longitud[2] = 34.3;
    longitud[3] = 10.1;
    longitud[4] = 64.3;

    latitud[0] = 3.1;
    latitud[1] = 32.1;
    latitud[2] = 2.1;
    latitud[3] = 89.1;
    latitud[4] = 21.1;

    struct timespec ti, tf;
    double elapsed, tC, tAsm;
    
    clock_gettime(CLOCK_REALTIME, &ti);
    cCalcularDistancias(longitud, latitud, N,ciudades);
    clock_gettime(CLOCK_REALTIME, &tf);
    tC = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    //tC = tf.tv_nsec-ti.tv_nsec;
    printf("Tiemplo de ejecuccion en nanosegundos en C : %f\n",tC);
    for(int i=0; i<N;i++)
        printf("%f  ",ciudades[i]);
    printf("\n");
    
    clock_gettime(CLOCK_REALTIME, &ti);
    asmCalcularDistancias(longitud, latitud, N, ciudades);
    clock_gettime(CLOCK_REALTIME, &tf);
    tAsm = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    //tAsm = tf.tv_nsec-ti.tv_nsec;
    printf("Tiemplo de ejecuccion en nanosegundos en C : %f\n",tAsm);
    for(int i=0; i<N;i++)
        printf("%f  ",ciudades[i]);
    printf("\n");
    double SpeedUp = (tC)/(tAsm);

    printf("El SpeedUp entre C y ASM es: %f\n",SpeedUp);

    return 0;
}

void cCalcularDistancias(float *longitud,float *latitud,int N,float *ciudades){
    for(int i=0; i<N;i++){
        ciudades[i] = sqrt(pow(longitud[i],2)+pow(latitud[i],2));
    }
}