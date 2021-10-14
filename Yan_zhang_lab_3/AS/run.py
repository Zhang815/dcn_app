from socket import socket, AF_INET, SOCK_DGRAM
import json

serversocket = socket(AF_INET, SOCK_DGRAM)
port_num = 53533
info = {}
serversocket.bind(('127.0.0.1', port_num))

def register(hostname, ip, type, ttl):
    c= {
    'TYPE': type,
    'VALUE': ip,
    'NAME': hostname,
    'TTL': ttl}
    index = type + ' ' + hostname
    info[index] = c
    jos=json.dumps('')
    return jos.encode()

def query(hostname, type):
    a = info[type + ' ' + hostname]
    fs_ip = a['VALUE']
    return str(fs_ip).encode()

def get_request(qmsg):
    msg = json.loads(qmsg.decode())
    if 'VALUE' in message:
        ip==Ture
        hostname = message['NAME']
        type = message['TYPE']
        ip = message['VALUE']
        ttl = message['TTL']
        return register(hostname, ip, type, ttl)
    else:
        ip==false
        hostname = message['NAME']
        type = message['TYPE']
        return query(hostname, type)
        
while True:
    q_message,c_address = serverSocket.recvfrom(2048)
    r_message = message.decode().split()
    if len(r_message) == 4:
        return_message = reg_host(r_message)
    elif len(r_message) == 2:
        return_message = query_address(r_message)
    else:
        return_message='error'
        
    serverSocket.sendto(return_message.encode(),c_address)
