section .data
    binstr db "10101010"
    res db 0

section .text
    global _start

_start:
    mov r15, binstr
    mov r14, 128
    mov r13, 2
    mov r12,0

mulbuc:
    mov al, [r15]
    sub al, 48      ;sub al, '0'
    mul r14         ; rax = rax*r14
    add r12, rax    ; r12 = r12+rax

sigpa:
    xor rdx,rdx     ;    mov rdx,0
    mov rax, r14
    div r13
    mov r14, rax
    inc r15
    cmp r14, 0
    jne mulbuc


mov [res], r12b
impresion:
	xor rcx, rcx
	mov r8, 10
	mov rcx, [res]
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
	
loopPrint:
	cmp rbx, 0
	je final
	dec rbx
	pop rcx
	
	add rcx, '0' ; 30h o 48, son equivalentes
	mov [res], rcx
	
    ;imprime el digito
	mov rax, 1
	mov rdi, 1
	mov rsi, res
	mov rdx, 1
	syscall
	jmp loopPrint
	
final:
	mov rax,60
	mov rdi, 0
	syscall


