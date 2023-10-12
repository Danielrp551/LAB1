	global asmCalcularAreaPoligono
	section .text

asmCalcularAreaPoligono:

; float <--  float *x,float *y,int N
; x --> rdi
; y --> rsi
; N --> rdx
; resultado <-- xmm0
	xorpd	xmm0,	xmm0
	xorpd	xmm1,	xmm1; suma1_momentaneo
    xorpd   xmm2,   xmm2; suma2_momentaneo
    xorpd   xmm3,   xmm3; suma
    xorpd   xmm4,   xmm4; el 2 a dividir
    mov r9, 2
    cvtsi2ss    xmm4,r9
    mov r8,rdx
    dec r8
	cmp	rdx,	0
	je	done
    xor rdx,rdx
next:
    movss   xmm3, [rdi + 4*rdx]; suma1 = x[i]   
    mulss   xmm3, [rsi + 4*(rdx+1)]; suma 1 = x[i]*y[i+1]
    addss   xmm1,   xmm3

    movss   xmm3, [rdi + 4*(rdx+1)]; suma2 = x[i+1]
    mulss   xmm3, [rsi + 4*(rdx)];    suma 2= x[i+1]*y[i]
    addss   xmm2,    xmm3

	;add	rdi,	4
    ;add rsi,    4 
	inc	rdx
	cmp rdx, r8
    jne next	
done:
    movss xmm3, [rdi + 4*(rdx)]
    mulss xmm3, [rsi]
    addss xmm1, xmm3; xmm1 = suma1 + x[N-1]*y[0]

    movss xmm3, [rdi]
    mulss xmm3, [rsi + 4*(rdx)]
    addss xmm2,xmm3; xmm2 = suma2 + x[0]*y[N-1]

    ucomiss xmm1,xmm2
    jb RestaNegativa
    subss xmm1, xmm2
    divss xmm1,xmm4
    movss xmm0,xmm1
    jmp fin
    RestaNegativa:
    subss xmm2,xmm1
    divss xmm2,xmm4
    movss xmm0,xmm2
    fin:
	ret

;    float suma1=0, suma2=0;
;    for(int i=0; i<N-1; i++){
;        suma1 += x[i]*y[i+1];
;        suma2 += x[i+1]*y[i];       
;    } 
;    suma1-= suma2;
;    suma1+= x[N-1]*y[0];
;    suma1-= x[0]*y[N-1];
;    return 0.5*(fabs(suma1));