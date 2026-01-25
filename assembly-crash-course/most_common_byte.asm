section .text
global _start
_start:
    push rbp
    mov rbp, rsp
    
    sub rsp, 512
    
    lea r10, [rbp-512]
    xor rcx, rcx
    
init_counters:
    mov word [r10 + rcx*2], 0
    inc rcx
    cmp rcx, 256
    jl init_counters
    
    xor rcx, rcx
    
count_bytes:
    cmp rcx, rsi
    jge find_max
    
    movzx rdx, byte [rdi + rcx]
    
    inc word [r10 + rdx*2]
    
    inc rcx
    jmp count_bytes
    
find_max:
    xor rdx, rdx
    xor rax, rax
    xor rcx, rcx
    
max_loop:
    cmp rdx, 0xff
    jg max_done
    
    movzx r8, word [r10 + rdx*2]
    
    cmp r8, rcx
    jle not_max
    
    mov rcx, r8
    mov rax, rdx
    
not_max:
    inc rdx
    jmp max_loop
    
max_done:
    mov rsp, rbp
    pop rbp
    ret