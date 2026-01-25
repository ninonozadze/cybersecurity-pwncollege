section .text
global _start
_start:
    mov eax, [rdi]
    cmp eax, 0x7f454c46
    jne else_if

    mov eax, [rdi+4]
    add eax, [rdi+8]
    add eax, [rdi+12]
    jmp bolo

else_if:
    cmp dword [rdi], 0x00005A4D
    jne bolo_else

    mov eax, [rdi+4]
    sub eax, [rdi+8]
    sub eax, [rdi+12]
    jmp bolo

bolo_else:
    mov eax, [rdi+4]
    imul eax, [rdi+8]
    imul eax, [rdi+12]

bolo: