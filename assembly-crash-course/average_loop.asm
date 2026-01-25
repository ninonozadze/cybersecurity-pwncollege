section .text
global _start
_start:
    mov rax, 0x0
    mov rcx, 0x0

cycle:
    add rax, [rdi + rcx*8]
    inc rcx
    cmp rcx, rsi
    jl cycle

    mov rdx, 0x0
    div rsi