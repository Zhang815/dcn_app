from socket import *
from flask import Flask,request,jsonify
import requests


app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)

@app.route('/fibonacci',methods=['Get'])
def fibo():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = int(request.args.get('as_port'))
    
    if  hostname and fs_port and number and as_ip and as_port:
        msg = "TYPE=A\nNAME={}".format(hostname)
        sock = socket(AF_INET, SOCK_DGRAM)
        c_sock.sendto(msg.encode(),(as_ip,53533))
        byte,address=client_socket.recvfrom(2048)
        info= json.loads(ip_address.decode())
        client_socket.close()
        r = requests.get("http://{}:{}fibonacci?number={}".format(value,fs_port,number))
        return jsonify(r.json(),200)
    else:
        
        return jsonify("error"), 404

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
