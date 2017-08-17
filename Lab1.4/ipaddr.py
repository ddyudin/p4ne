#import

from ipaddress import IPv4Network
import random

#create empty tulip
list_of_networks =[]

#define new class
class IPv4RandomNetwork(IPv4Network):
    def __init__(self, na="0.0.0.0", m="/0"):
        IPv4Network.__init__(self,(random.randint(0x0B000000, 0xDF000000),random.randint(8, 24)),strict=False)
#define new method - returns ip adreess + mask(moved to higher 32 bit)
    def key_value(self):
        return int(self.network_address._ip) + (int(self.netmask._ip)*2**32)

# define sort function
def yahoo(x):
    return x.key_value()

#create and print source list of ip address
for i in range (0,50):
    list_of_networks.append(IPv4RandomNetwork())
print('Source list')
for y in list_of_networks:
    print(y)

#do sort
l2=sorted(list_of_networks, key=yahoo)

#print result
print(''
      '')
print('sorted list')
for x in l2:
    print(x)


#sorted(последовательность, key=функция) — возвращает отсортированную последовательность