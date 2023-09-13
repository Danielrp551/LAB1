; Para ensamblar ejecutar:
; nasm -f elf64 helloworldlen.asm -o helloworldlen.o
; Para enlazar ejecutar:
; ld helloworldlen.o -o helloworldlen
; Para correr el ejecutable:
; ./helloworldlen
section .data
    N   dd 3
section .bss
    res resd 1
section .text
    global _start

_start:
    mov r15, 0      ; s = 0
    mov r14, 0      ; i = 0
    mov r13, [N]    

comp_i_N:
    cmp r14, r13
    jg  salvar_s

cuerpo_bucle:
    mov rax, r14
    imul rax
    add r15, rax
    inc r14
    jmp comp_i_N

salvar_s:
    mov [res], r15

fin:
    mov rax, 60
    mov rdi, 0
    syscall