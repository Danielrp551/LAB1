section .data
    mensaje db "Hola mundo",0

section .bss
    inversa resb 20

section .text
    global _start

_start:
    mov rax, mensaje
    mov rbx,0

_countLoop:
    inc rax
    inc rbx
    mov cl, [rax]
    cmp cl,0
    jne _countLoop

    mov r9, inversa
    
_reverse:
    dec rax
    mov r10,[rax]
    mov [r9], r10
    inc r9
    cmp rax, mensaje
    jne _reverse

    mov [r9], byte 10
    inc rbx
imprimir:
    mov rax,1
    mov rdi,1
    mov rsi, inversa
    mov rdx,rbx
    syscall
fin:
    mov rax, 60
    mov rdi,0
    syscall


