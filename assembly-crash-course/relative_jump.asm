section .text
global _start
_start:
    jmp Instruction
    %rep 0x51
    nop 
    %endrep
Instruction:
    mov rax, 0x1