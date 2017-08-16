#получение перечня интерфейсов

# Импортировать только High-level API
from pysnmp.hlapi import *

#Type and Version request
result = getCmd(SnmpEngine(),
                CommunityData("public", mpModel=0), #CommunityData(community_name, mpModel=0)
                UdpTransportTarget(("10.31.70.107", 161)), #UdpTransportTarget((ipaddr_string, port_int))
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
#Print result
for x in result:
    v=x[3]
    print(v)
    for y in v:
        for z in y:
            print(z)

#Interface request
result2 = nextCmd(SnmpEngine(),
                CommunityData("public", mpModel=0), #CommunityData(community_name, mpModel=0)
                UdpTransportTarget(("10.31.70.107", 161)), #UdpTransportTarget((ipaddr_string, port_int))
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),lexicographicMode=False )

#Print result
for x in result2:
    v=x[3]
    print(v)
    for y in v:
        for z in y:
            print(z)





#snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0) # По имени MIB-переменной
# snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2') # По значению MIB-переменной
# result — список кортежей (errorIndication, errorStatus, errorIndex, varBinds)
#varBinds — список из строк, которые вернуло сетевое устройство в ответ на запрос
