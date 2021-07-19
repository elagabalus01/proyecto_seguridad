from xmlrpc.server import SimpleXMLRPCServer
from utils.get_host_ip import get_local_ip

def registrar(host):
    print(f"Nuevo host conectado {host}")
    return True

host=str(get_local_ip())
port=9001
server = SimpleXMLRPCServer((host, port))
server.register_function(registrar, 'registrar')

try:
    print("Corriendo servidor de registro")
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
