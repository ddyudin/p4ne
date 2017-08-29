from flask import *
import sys
import glob
import re


hosts = {}
# get file list and open file
for file_name in glob.glob(('f:\\Seafile\\p4ne_training\\config_files\\*.txt')):
    hosts[file_name] = {}
    hosts[file_name]['addresses'] = []
    with open(file_name) as f:
        for imp_str in f:
            s = re.match('^hostname (.+)', imp_str)
            if s :
                hosts[file_name]['name'] = s.group(1)
                continue
            s = re.match('^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', imp_str)
            if s:
                hosts[file_name]['addresses'].append({'ip':s.group(1), 'mask':s.group(2)})

app = Flask(__name__)

@app.route('/')
def helpy():
    return 'Краткая справка об использовании'

@app.route('/python')
def pyth():
    return jsonify(repr(sys.__dict__))

@app.route('/configs')
def host_info():
    r = []
    for h in hosts.keys():
        r.append(hosts[h]['name'])
    return jsonify(r)

@app.route('/configs/<hostname>')
def ip_info(hostname):
    for h in hosts.keys():
        if hosts[h]['name'] == hostname:
            return jsonify(hosts[h]['addresses'])
    return jsonify("Not found")

if __name__ == '__main__':
        app.run(debug=True)