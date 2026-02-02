# Shellcode Injection


This project demonstrates a shellcode injection workflow using assembly.


**Course:** https://pwn.college/cse466-f2023/shellcode-injection/

---

## Example: 

## Create an Assembly Source File

Create a file called **`shellcode_injection.s`**

---

## Build Shellcode

Compile the assembly file without linking the standard C library:

```bash
gcc -nostdlib shellcode_injection.s
```

---

## Extract Raw Shellcode

```bash
objcopy -O binary --only-section=.text ./a.out ./asm.bin
```

---

## Run the Challenge

Pipe the raw shellcode into the challenge binary

```bash
cat asm.bin | /challenge/binary-exploitation-basic-shellcode
```