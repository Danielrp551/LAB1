

;AsmavgFilter(float *x,int N,float *y)

	global AsmavgFilter
	section .text

AsmavgFilter:
; float *x,int N,float *y
; x --> rdi
; N --> rsi
; y --> rdx
; 
	xorpd	xmm0,	xmm0; n-1
	xorpd	xmm1,	xmm1; n
    xorpd   xmm2,   xmm2; n+1
    xorpd   xmm3,   xmm3
    mov r8,rsi
    mov r9, 3
    cvtsi2ss    xmm3, r9    
	cmp	rsi,	0
	je	done
    xor rsi,rsi
next:
    cmp rsi,r8
    jne NoEsIndiceFinal
    ;En caso es indice final
    movss xmm0, [rdi - 4]; n-1 = x[n-1]
    movss xmm1, [rdi] ; n = x[n]
    movss xmm2, [rdi]   ; n= x[n]
    jmp   calcularY
    NoEsIndiceFinal:
    cmp rsi, 0
    jne NoesIndiceInicial
    movss xmm0, [rdi]   ; n-1 = n
    movss xmm1, [rdi]   ; n = n
    movss xmm2, [rdi+ 4]; n= n+1
    jmp calcularY
    NoesIndiceInicial:
	movss	xmm0,	[rdi -4] ; n-1 = x[n-1]
    movss   xmm1,   [rdi]  ;    n = x[n]
    movss   xmm2,   [rdi +4]; n+1  = x[n+1]
    calcularY:
    addss   xmm0, xmm1
    addss   xmm0, xmm2
    divss   xmm0, xmm3

	add	rdi,	4
    movss	[rdx],	xmm0
    add rdx,    4   
	inc	rsi
    cmp rsi, r8
	jne next
done:
	ret


;    int nMenos1, n, nMas1;
;    for(int i=0; i<N;i++){
;        if(i==0){
;            nMenos1 = x[i];
;            n = x[i];
;            nMas1 = x[i+1];
;        }
;        if(i==N-1){
;            nMenos1 = x[i-1];
;            n = x[i];
;            nMas1 = x[i];   
;        }
;        nMenos1 = x[i-1];
;        n = x[i];
;        nMas1 = x[i+1];  
;        y[i] = (nMenos1+n+nMas1)/3;
;    }