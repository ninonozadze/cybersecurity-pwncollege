section .text
global _start
_start:
    mov rax, [rsp]
    mov rbx, [rsp + 8]
    mov rcx, [rsp + 16]
    mov rdx, [rsp + 24]

    add rax, rbx
    add rax, rcx
    add rax, rdx

    shr rax, 2
    push rax