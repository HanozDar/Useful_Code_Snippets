import pwn
from pwn import *

p = process('./binary_name') # CHANGE THIS TO THE BINARY NAME

'''
##### INPUT THE PATH AND OPTIONS TO GET TO THE BUFFER OVERFLOW HERE. ######

p.sendline()
p.recv()
p.recvuntil()
Depending on the binary
###########################################################################
'''
x = 100 # CHANGE THIS TO THE SIZE OF THE BUFFER THAT NEEDS TO BE OVERFLOWED
payload = cyclic(x,n=4) # CHANGE THE VALUE OF n TO 8 IF YOU WANT TO FIND THE OFFSET IN x64
p.sendline(payload)

p.wait()
core = p.corefile

offset = cyclic_find(core.fault_addr)
log.success("We have found the offset at location " + str(offset))

