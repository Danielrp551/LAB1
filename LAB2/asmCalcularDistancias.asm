	global asmCalcularDistancias
	section .text

asmCalcularDistancias:
; float *longitud,float* latitud,int N,float * ciudades
; longitud --> rdi
; latitud --> rsi
; N --> rdx
; ciudades -->rcx
	xorpd	xmm0,	xmm0
	xorpd	xmm1,	xmm1
	cmp	rdx,	0
	je	done
next:
	movss	xmm0,	[rdi] ; lontigud[i]
    movss   xmm1,   [rsi]  ;latitud[i]
	mulss	xmm0,	xmm0
    mulss   xmm1,   xmm1
	addss	xmm1,	xmm0
	add	rdi,	4
    add rsi,    4
    sqrtss	xmm1,	xmm1
    movss	[rcx],	xmm1
    add rcx,    4   
	sub	rdx,	1
	jnz	next	
done:
	ret