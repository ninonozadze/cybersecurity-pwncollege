.intel_syntax noprefix
.global _start
_start:


// int fd = open("f", 0);
push 'f'
mov rdi, rsp
mov al, 2
xor esi, esi
syscall

// read(fd, buff, 100);
xchg eax, edi
xor eax, eax
push rsp
pop rsi
mov dl, 100
syscall

// write(1, buff, 100);
mov al, 1
mov dil, 1
syscall