section .text
global _start
_start:
    mov rdx, 0x0
    mov rax, rdi
    div rsi
    mov rax, rdx