section .text
global _start
_start:
        cmp rdi, 0
        je tavshive_nuli
 
      	mov rax, 0x0

cycle:
        mov cl, byte [rdi + rax]
      	cmp cl, 0
       	je bolo

        inc rax
      	jmp cycle

tavshive_nuli:
        mov rax, 0x0

bolo: