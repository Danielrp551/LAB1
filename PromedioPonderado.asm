
; Programa getname.asm
; Para ensamblar ejecutar:
; nasm -f elf64 getname.asm -o getname.o
; Para enlazar ejecutar:
; ld getname.o -o getname
; Para correr el ejecutable:
; ./getname


section .data
	;Mensaje
	preguntaPracticas db "Peso de las practicas: " 
	lenPracticas equ $ - preguntaPracticas 

    preguntaLaboratorios db "Peso de los laboratorios: " 
	lenLaboratorios equ $ - preguntaLaboratorios

    preguntaParcial db "Peso de el examen parcial :  " 
	lenParcial equ $ - preguntaParcial

    preguntaFinal db "Peso de el examen final: " 
	lenFinal equ $ - preguntaFinal

    resultados db "Nota final calculada : "
    lenResultados equ $ - resultados
	
	arregloNOtas dq 15, 13 , 17, 20
    arregloPesos times 4 dq 0

    notafinal dq 0
    peso_Practica dq 0
    peso_Lab dq 0
    peso_Parcial dq 0
    peso_Final dq 0

    ;auxiliar
    char dq 0

section .text
    global _start


_start:

;WRITE 
    mov rax, 1
	mov rdi, 1
	mov rsi, preguntaPracticas
	mov rdx, lenPracticas
	syscall
;READ
    mov rax, 0
	mov rdi, 0
	mov rsi, peso_Practica
	mov rdx, 1
	syscall

;READ  lee algo
    mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall

;WRITE 
    mov rax, 1
	mov rdi, 1
	mov rsi, preguntaLaboratorios
	mov rdx, lenLaboratorios
	syscall
;READ
    mov rax, 0
	mov rdi, 0
	mov rsi, peso_Lab
	mov rdx, 1
	syscall

;READ  lee algo
    mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall

;WRITE 
    mov rax, 1
	mov rdi, 1
	mov rsi, preguntaParcial
	mov rdx, lenParcial
	syscall
;READ
    mov rax, 0
	mov rdi, 0
	mov rsi, peso_Parcial
	mov rdx, 1
	syscall

;WRITE 
    mov rax, 1
	mov rdi, 1
	mov rsi, preguntaFinal
	mov rdx, lenFinal
	syscall
;READ  lee algo
    mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall
;READ
    mov rax, 0
	mov rdi, 0
	mov rsi, peso_Final
	mov rdx, 1
	syscall





;ALISTO VARIABLES

        
        
    mov rcx,[peso_Practica]
    sub rcx, '0'
    mov [arregloPesos], rcx
    mov rcx,[peso_Lab]
    sub rcx, '0'
    mov [arregloPesos+8], rcx
    mov rcx,[peso_Parcial]
    sub rcx, '0'
    mov [arregloPesos+16], rcx
    mov rcx,[peso_Final]
    sub rcx, '0'
    mov [arregloPesos+24], rcx    

    mov rbx, 4
    xor rcx,rcx
    xor rdx,rdx

for:

    cmp rcx,rbx
    je div_nota
    mov rdx, [arregloNOtas + 8*rcx]
    mov rax, [arregloPesos + 8*rcx]
    mul rdx ;rax = rax*rcx
    add [notafinal], rax
    inc rcx
    jmp for


div_nota:
    mov rax, [notafinal]
    mov r8, 10
    div r8
    cmp rdx, 5
    jl no_aproximar
    inc rax
no_aproximar:
    mov [notafinal], rax
    xor rdx,rdx

impresion:
	xor rcx, rcx
	mov r8, 10
	mov rcx, [notafinal]
	mov rbx, 0
	xor rdx, rdx
	
division:
	mov rax, rcx
	cmp rax, r8
	jl auxiliar
	xor rdx, rdx
	div r8
	inc rbx
	push rdx
	mov rcx, rax
	jmp division
	
auxiliar:
	push rax
	inc rbx
	
;IMPRIMIR TEXTO DE SALIDA
    mov rax, 1
	mov rdi, 1
	mov rsi, resultados
	mov rdx, lenResultados
	syscall



loopPrint:
	cmp rbx, 0
	je final
	dec rbx
	pop rcx
	
	add rcx, '0' ; 30h o 48, son equivalentes
	mov [notafinal], rcx
	
    ;imprime el digito
	mov rax, 1
	mov rdi, 1
	mov rsi, notafinal
	mov rdx, 1
	syscall
	jmp loopPrint
	
final:
	mov rax,60
	mov rdi, 0
	syscall



