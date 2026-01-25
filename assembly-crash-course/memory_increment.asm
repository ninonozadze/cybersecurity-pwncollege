section .text
global _start
_start:
	mov rax, [0x404000]
	add qword [0x404000], 0x1337