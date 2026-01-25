section .text
global _start
_start:
    cmp rdi, 0
    je return_zero

    xor rax, rax

loop_start:
    cmp byte [rdi], 0
    je return

    cmp byte [rdi], 0x5a
    jg skip_conversion

    push rdi
    push rax

    movzx rdi, byte [rdi]

    mov r10, 0x403000
    call r10

    pop r11
    pop rdi
    mov [rdi], al
    mov rax, r11

    inc rax

skip_conversion:
    inc rdi

    jmp loop_start

return_zero:
    xor rax, rax

return:
    ret