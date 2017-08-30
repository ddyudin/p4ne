import requests, json, pprint
from flask import *

#web-server
app = Flask(__name__)

#show list of hosts
@app.route('/hosts')
def hosts1():
    return jsonify(hosts())

#show list of devices
@app.route('/devices')
def devices1():
    return jsonify(devices())

#show topology
@app.route('/api/topology')
def topology1():
    return jsonify(topology())

#show net
@app.route("/")
def index():
    return render_template("topology.html")

#recieve new ticket
def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    #pprint.pprint(json.dumps(response.json()))
    return response.json()['response']['serviceTicket']

#func get hosts
def hosts():
    controller = 'devnetapi.cisco.com/sandbox/apic_em'
    url = 'https://' + controller + '/api/v1/host'
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json() ['response']

#func get devices
def devices():
    controller = 'devnetapi.cisco.com/sandbox/apic_em'
    url = 'https://'+ controller + '/api/v1/network-device'
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json() ['response']

#func get topology
def topology():
    controller = 'devnetapi.cisco.com/sandbox/apic_em'
    url = 'https://' + controller + '/api/v1/topology/physical-topology'
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json() ['response']


if __name__ == '__main__':
#get new ticket from cisco
    ticket = new_ticket()
#run web-server
    app.run(debug=True)
