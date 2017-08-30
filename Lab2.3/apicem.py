import requests, json, pprint
from flask import *

app = Flask(__name__)

@app.route('/hosts')
def hosts1():
    return jsonify(hosts())

@app.route('/devices')
def devices1():
    return jsonify(devices())

@app.route('/api/topology')
def topology1():
    return jsonify(topology())

@app.route("/")
def index():
    return render_template("topology.html")


def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    #pprint.pprint(json.dumps(response.json()))
    return response.json()['response']['serviceTicket']

def hosts():
    controller = 'devnetapi.cisco.com/sandbox/apic_em'
    url = 'https://' + controller + '/api/v1/host'
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json() ['response']

def devices():
    controller = 'devnetapi.cisco.com/sandbox/apic_em'
    url = 'https://'+ controller + '/api/v1/network-device'
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json() ['response']

def topology():
    controller = 'devnetapi.cisco.com/sandbox/apic_em'
    url = 'https://' + controller + '/api/v1/topology/physical-topology'
    header = {"content-type": "application/json","X-Auth-Token":ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json() ['response']

if __name__ == '__main__':
    ticket = new_ticket()
    app.run(debug=True)
