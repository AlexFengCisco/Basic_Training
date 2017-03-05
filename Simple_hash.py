'''
Created on May 7, 2014

@author: AlexFeng
'''

ip_prefix_list=['192.168.1.0','192.168.2.0','192.168.3.0','172.16.1.0','172.16.2.0']
if_index=['0/1','0/1','1/2','0/2','0/2']

fib_index=map(hash,ip_prefix_list)
print fib_index

fib_bank_01={k:v for k,v in zip(fib_index,ip_prefix_list)}
fib_bank_02={k:v for k,v in zip(fib_index,if_index)}  #install to the real useful bank  hash_vaule to interface_index table

print fib_bank_01
print fib_bank_02


#--------search specific ip prefix and get the output interface Index from fib

prefix='192.168.2.0'
result=fib_bank_02[hash(prefix)]

print "ip prefix %s should be forward via interface %s"%(prefix,result)