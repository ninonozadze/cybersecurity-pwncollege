section .text
global _start
_start:
    jmp Instruction
    %rep 0x51
    nop 
    %endrep
Instruction:
    pop rdi
    mov rax, 0x403000
    jmp rax