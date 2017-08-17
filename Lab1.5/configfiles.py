import glob

list_of_address = []
# get file list
flist = glob.glob(('f:\\Seafile\\p4ne_training\\config_files\\*.txt'))

# open file
for name in flist:
    with open(name) as f:
        str_list = list(f)
# print(str_list)
for adr in str_list:
    if adr.find('ip address ') > 0:
        list_of_address.append(adr.replace('ip address ', '').strip())

print(sorted(list(set(list(list_of_address)))))
