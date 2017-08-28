import glob
import re

#Написать функцию - классификатор, которая на вход принимает произвольную строку и возвращает кортеж:
def classification(inp_str):
    # для строк вида ip address 192.168.1.1 255.255.255.0
    s = re.match('^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', inp_str)
    if  s:
        return ('IP', s.group(1), s.group(2))
    # для строк вида interface GigabitEthernet0
    s= re.match('^interface (.+)', inp_str)
    if s:
        return ('INT', s.group(1))
    # для строк вида hostname xxx
    s = re.match('^hostname (.+)', inp_str)
    if s:
        return ('HOST', s.group(1))
    else: #во всех остальных случаях
        return ('UNCLASSIFIED',) #кортеж из одного элемента

# get file list and open file
for name in glob.glob(('f:\\Seafile\\p4ne_training\\config_files\\*.txt')):
    with open(name) as f:
        for imp_str in f:
            c = classification(imp_str)
            if c[0] == 'IP': #removing 'UNCLASSIFIED'
                print(c)

