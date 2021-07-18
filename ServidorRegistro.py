from xmlrpc.server import SimpleXMLRPCServer

def registrar(host):
    print(f"Nuevo host conectado {host}")

server = SimpleXMLRPCServer(('localhost', 9000))
server.register_function(registrar, 'registrar')

try:
    print("Corriendo servidor de registro")
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')