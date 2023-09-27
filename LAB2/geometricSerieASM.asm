

;float geometricSerie (int a, int N, float x)

	global geometricSerieASM
	section .text

geometricSerieASM:
; int a, int N, float x
; a --> rdi
; N --> rsi
; x --> xmm0
; 
	xorpd	xmm1,	xmm1; resultado = 0
    xorpd   xmm2,   xmm2; resultado del pow(x,n)
    xorpd   xmm4,   xmm4;  
    cvtsi2ss   xmm3, rdi  ; xmm3 <- a  
    mov r8,rsi
    ;inc r8   
	cmp	rsi,	0
	je	done
    mov rsi, 1
next:
    movss xmm2, xmm0; resultado del pow(x,n) = x por ahora
    movss xmm4, xmm0;     
    mov r10, rsi
    calcularPow:
    dec r10
    cmp r10, 0
    je  TerminoPow
    mulss xmm2, xmm4 ; x= x*x
    jmp calcularPow
    TerminoPow:
    addss xmm1, xmm2 ; resultado += pow(x,n) 
	inc	rsi
    cmp rsi, r8
	jne next
done:
    cvtsi2ss xmm4, rdi
    mulss   xmm1, xmm4
    addss   xmm1, xmm4      
    movss   xmm0, xmm1
fin:
	ret


;   float resultado=0;
;    for(int i=0; i<N;i++){
;        resultado += pow(x,i);
;    }    
;    return resultado*a;