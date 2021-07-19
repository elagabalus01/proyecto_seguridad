import xmlrpc.client
import sys
try:
    host=sys.argv[1]
    proxy = xmlrpc.client.ServerProxy(f'http://{host}:9000')
    try:
        print('Use Control-C to exit')
        while True:
            try:
                comando=input()
                comando=comando.split(' ')
                print(comando)
                result=getattr(proxy, 'command')(comando)
                print("Resultado:")
                print(result)
            except xmlrpc.client.Fault as e:
                print(f"Cliente fault {e.faultString}")
                # print(help(e))
            except Exception as e:
                print(f"Error al ejecutar el comando {e}")
                print(type(e))
    except KeyboardInterrupt:
        print('Exiting')

except IndexError:
    print("Indica la dirección del servidor")
