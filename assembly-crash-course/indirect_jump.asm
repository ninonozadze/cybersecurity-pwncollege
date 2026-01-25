section .text
global _start
_start:
    cmp rdi, 3
    ja default_case

    shl rdi, 3
    add rsi, rdi

    mov rax, [rsi]
    jmp rax

default_case:
    mov rax, [rsi+32]
    jmp rax