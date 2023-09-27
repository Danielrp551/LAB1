#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

extern float geometricSerieASM (int a, int N, float x);
float geometricSerie (int a, int N, float x);


//; nasm -f elf64 asmFloatInnerProd.asm -o asmFloatInnerProd.o
// gcc asmFloatInnerProd.o floatInnerProd.c -o floatInnerProd -lm
// ./floatInnerProd


int main(int argc, char const *argv[]){
    
    clock_t start, stop;

    float timeC, timeASM;
    float yC, yASM;
    int N = 100;
    int a = 3;
    float x = 0.2;

    /* Validar que el usuario ingreso el valor de N y que sea mayor a 0 */
    if (argc < 4){
        printf("Utilizando valores default x = 0.2, a = 3, N = 100\n");
    } else{
        x = atof(argv[1]);
        a = atoi(argv[2]);
        N = atoi(argv[3]);
        printf("Utilizando valores x = %.2f, a = %d, N = %d\n", x, a, N);
    }

    /* FIXME: llamar a las funciones en C y ASM y medir los tiempos de cada una para calcular el SU */
    struct timespec ti, tf;
    double elapsed, tC, tAsm;
    
    clock_gettime(CLOCK_REALTIME, &ti);
    yC = geometricSerie(a,N,x);
    clock_gettime(CLOCK_REALTIME, &tf);
    tC = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    //tC = tf.tv_nsec-ti.tv_nsec;
    printf("Tiemplo de ejecuccion en nanosegundos en C : %f\n",tC);
    printf("Resultado del calculo en C: %f\n", yC);

    clock_gettime(CLOCK_REALTIME, &ti);
    yASM =geometricSerieASM(a,N,x);
    clock_gettime(CLOCK_REALTIME, &tf);
    tAsm = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    //tC = tf.tv_nsec-ti.tv_nsec;
    printf("Tiemplo de ejecuccion en nanosegundos en ASM : %f\n",tAsm);
    printf("Resultado del calculo en ASM: %f\n\n", yASM);

    /* FIXME: cálculo del valor de la sumatoria utilizando la división a/1-x */
    printf("Resultado de a/1-x : %f\n", (double)a/(1-x));


    /* FIXME: impresiones de diferencia de resultados y SU */




    return 0;
}


float geometricSerie (int a, int N, float x){
/* FIXME: calcular la sumatoria de la serie geometrica */
    float resultado=0;
    for(int i=0; i<N;i++){
        resultado += pow(x,i);
    }    
    return resultado*a;
}
