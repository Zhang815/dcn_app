from flask import Flask,request
from socket import *
import json


app = Flask(__name__)

def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)
        

@app.route('/register', methods=['PUT'])
def register():
    hostname = request.get_json.get('hostname')
    ip = request.get_json.get('ip','127.0.0.1')
    as_ip = request.get_json.get('as_ip','127.0.0.1')
    as_port = int(request.get_json.get('as_port'))
    server_name,server_port = as_ip,53533
    fs_socket = socket(AF_INET, SOCK_DGRAM)
    dns_request = {'TYPE': 'A','NAME': hostname,'VALUE': ip,'TTL': 10
    }
    message = json.dumps(dns_request)
    fs_socket.sendto(message.encode(), (server_name, server_port))
    message, server_address = fs_socket.recvfrom(2048)
    fs_socket.close()
    return message.decode()
    
@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    if not number :
        return jsonify('error'), 400
    
    return jsonify(f(int(number))), 200
        

app.run(host='0.0.0.0',
        port=9090,
        debug=True)
