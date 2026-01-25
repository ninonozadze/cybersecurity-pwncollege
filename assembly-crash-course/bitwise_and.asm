section .text
global _start
_start:
    xor rax, rax
    and rdi, rsi
    or rax, rdi