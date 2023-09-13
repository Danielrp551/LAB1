


; Programa getname.asm
; Para ensamblar ejecutar:
; nasm -f elf64 getname.asm -o getname.o
; Para enlazar ejecutar:
; ld getname.o -o getname
; Para correr el ejecutable:
; ./getname


section .data
	;Mensaje
	pregunta db "Ingrese los numeros: " 
	lenPregunta equ $ - pregunta 

    resultado db "La solucion es : "
    lenResultados equ $ - resultado

    signo_menos db " -"
    lenSigno equ $ - signo_menos

    valor_a dq 0
    valor_b dq 0
    valor_c dq 0
    result dq 0
    ;auxiliar
    char dq 0

section .text
    global _start


_start:


;WRITE 
    mov rax, 1
	mov rdi, 1
	mov rsi, pregunta
	mov rdx, lenPregunta
	syscall
;READ
    mov rax, 0
	mov rdi, 0
	mov rsi, valor_a
	mov rdx, 1
	syscall
;READ
    mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall
;READ
    mov rax, 0
	mov rdi, 0
	mov rsi, valor_b
	mov rdx, 1
	syscall
;READ
    mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall
;READ
    mov rax, 0
	mov rdi, 0
	mov rsi, valor_c
	mov rdx, 1
	syscall

;INICIALIZA
    xor rbx, rbx
    xor rax, rax
    xor rcx,rcx
    
    mov rbx, [valor_b]
    sub rbx,'0'
    pare1:
    mov rax, [valor_b]
    sub rax,'0'
    pare2:
    mul rbx ; rax = rax*rbx  --> b^2
    pare3:
    mov rbx, rax

    mov rcx, [valor_a]
    sub rcx, '0'
    mov rax, 4
    mul rcx ; rax = 4*a
    pare4: 
    mov rcx, [valor_c]
    sub rcx,'0'
    mul rcx ; rax = 4*a*c
    mov rcx, rax

    sub rbx, rcx
    cmp rbx,0
    jl resultado_negativo
    ;resultado_positivo:
    ;sub rbx, rcx
    ;hasta aqui tengo el numero


    mov [result], rbx
    mov r11, 0
    jmp impresion

    resultado_negativo:
    not rbx
    inc rbx
    mov r11, 1 ;Para poner el signo
    mov [result], rbx

    impresion:
	xor rcx, rcx
	mov r8, 10
	mov rcx, [result]
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
	mov rsi, resultado
	mov rdx, lenResultados
	syscall

;CMP CON EL SIGNO
    cmp r11, 0
    je loopPrint
    ;imprimo el signo
    mov rax,1
    mov rdi,1
    mov rsi, signo_menos
    mov rdx, lenSigno
    syscall

loopPrint:
	cmp rbx, 0
	je final
	dec rbx
	pop rcx
	
	add rcx, '0' ; 30h o 48, son equivalentes
	mov [result], rcx
	
    ;imprime el digito
	mov rax, 1
	mov rdi, 1
	mov rsi, result
	mov rdx, 1
	syscall
	jmp loopPrint
	
final:
	mov rax,60
	mov rdi, 0
	syscall


