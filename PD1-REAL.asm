; Programa getname.asm
; Para ensamblar ejecutar:
; nasm -f elf64 getname.asm -o getname.o
; Para enlazar ejecutar:
; ld getname.o -o getname
; Para correr el ejecutable:
; ./getname

section .data
    question db "Ingrese un numero para n : ",10
    lenq equ $ - question
    resultado db "La solucion es: ",5
    leng equ $ - resultado
    espacio db " "
    lenj equ $ - espacio

    number dq 0
    solution dq 0



section .text
    global _start

;WRITE
_start:
    mov rax, 1
	mov rdi, 1
	mov rsi, question
	mov rdx, lenq
	syscall

;READ
	mov rax, 0
	mov rdi, 0
	mov rsi, number
	mov rdx, 1
	syscall

    ;Los corchetes me hace mover el valor de number, no su dirección
    mov rcx, [number]
    sub rcx, 30H ; le resto 48 
;CALCULAR EL RESULTADO
countloop:
    mov rax, rcx
    mul rcx, ; rax = rax*rcx
    add [solution],rax
    dec rcx
    cmp rcx,0
    jne countloop



; WRITE
	mov rax, 1
	mov rdi, 1
	mov rsi, resultado
	mov rdx, leng
	syscall

test: ;pushea en pila el resultado
    xor rcx, rcx ; rcx lo pongo a 0
    mov r8,10
    mov rcx, [solution]
    mov rbx, 0
    xor rdx, rdx 

division:
    mov rax, rcx
    cmp rax, r8 ;si el numero es un 1 digito, es decir, menor a 10
    jl aux ;jump lower : salta si rax es menor a r8(10) 

    div r8 ;rdx residuo rax cociente
    inc rbx 
    push rdx

    mov rcx, rax
    jmp division

aux:
    push rax
    inc rbx

loopprint:
    cmp rbx,0
    je final
    dec rbx
    pop rcx 

    add rcx, 30H
    mov [solution],rcx
    
    

; WRITE
	mov rax, 1
	mov rdi, 1
	mov rsi, solution
	mov rdx, 1
	syscall
    jmp loopprint

;WRITE ESPACIO 

	mov rax, 1
	mov rdi, 1
	mov rsi, espacio
	mov rdx, lenj
	syscall

final:
; EXIT
	mov rax, 60
	mov rdi, 0
	syscall

