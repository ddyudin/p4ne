import glob
import re
import ipaddress

#from openpyxl import #найти функции создания книги, листа, записи на лист

#function to find ip
def classification(inp_str):
    # для строк вида ip address 192.168.1.1 255.255.255.0
    s = re.match('^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', inp_str)
    if  s:
        return (s.group(1), s.group(2))
    else:
        return False

#empty dic
list_of_address = {}
#list_of_networks =[]
# get file list and open file
for name in glob.glob(('f:\\Seafile\\p4ne_training\\config_files\\*.txt')):
    with open(name) as f:
        for imp_str in f:
            netaddr = classification(imp_str)
            if netaddr is not False:
#                list_of_address [netaddr[0]] = netaddr[1]
#                list_of_networks = netaddr[0] + '/' + netaddr[1]
#                list_of_networks = (ipaddress.ip_network(netaddr[0] + '/' + netaddr[1], strict = False))
#                list_of_networks.append(ipaddress.ip_network(netaddr[0] + '/' + netaddr[1], strict = False))
                list_of_address = {netaddr[0]:{'mask':netaddr[1]}, 'net': ipaddress.ip_network(netaddr[0] + '/' + netaddr[1], strict = False)}
                print(list_of_address.keys(), list_of_address.values())
exit(1)
list_to_find = list_of_address
print ('NETWORK\t\t\tMASK\t\t\tGATEWAY')
#exit(1)

for addr in list_of_address.keys():
    for to_find in list_to_find.keys():
        if ipaddress.ip_address(to_find) in ipaddress.ip_network(addr +'/'+list_of_address[addr], strict = False):
          #  print(ipaddress.ip_network(addr +'/'+list_of_address[addr], strict = False))
            print('%s\t\t\t%s\t\t\t%s' %ipaddress.ip_network(addr +'/'+list_of_address[addr], strict = False), list_of_address[to_find], to_find)
    #print('%s\t\t\t%s\t\t\t%s' %addr, list_of_address[addr], addr)



#    network = ipaddress.ip_network(addr + '/' + list_of_address[addr], strict=False))
    #print(network, list_of_networks [0])
#    for y in list_of_networks:
#        if list_of_networks == network:
#            print(network, list_of_address[addr], addr)
 #       else:
 #           print(addr, list_of_address[addr])
#    list_of_networks = ipaddress.ip_network(list_of_address.(), strict = False)

#for y in list_of_networks:
#    print (list_of_networks)

#print(sorted(list(set(list_of_address))))