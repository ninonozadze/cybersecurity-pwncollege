section .text
global _start
_start:
    and rax, 0x1
    and rdi, 1
    xor rax, rdi