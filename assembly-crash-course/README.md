# Assembly Crash Course

**Course:** https://pwn.college/computing-101/assembly-crash-course/

---

## Example: Create an Assembly Source File

Create a file called **`set_register.asm`**:

```bash
cat > set_register.asm << 'EOF'
section .text
global _start

_start:
    mov rdi, 0x1337
EOF
```

---

## Build the Program

Assemble and link the program:

```bash
nasm -f elf64 set_register.asm -o set_register.o
ld set_register.o -o set_register
chmod +x set_register
```

**Explanation**

* **`nasm -f elf64`** - assembles the source file into an ELF64 object file
* **`ld`** - links the object file into an executable
* **`chmod +x`** - makes the binary executable

---

## Run the Program

Execute the program using the challenge runner:

```bash
/challenge/run set_register
```
