from pwn import *

elf=ELF('./ROP_LEVEL0')
p=process('/ROP_LEVEL0')
rop=ROP(elf)


