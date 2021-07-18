import xmlrpc.client
proxy = xmlrpc.client.ServerProxy('http://192.168.1.2:9000')

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
