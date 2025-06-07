import argparse
import socket
import sys

def parse_arguments():

    # Creamos un parser de argumentos con una breve descripción del script
    parser = argparse.ArgumentParser(description="TCP client: connect to a server and send a message.",
    epilog="Example = python tcp_client.py 127.0.0.1 8080"
    )

    # añadimos los argumentos posicionales llamados 'ip' y 'port' con el tipo de dato al que corresponden
    parser.add_argument('ip', type=str, help="IP address of the server to connect")
    parser.add_argument('port', type=int, help="TCP port of the server")

    # Comprobamos si no se han pasado argumentos al script (solo el nombre del archivo)
    if len(sys.argv) <= 1:
        # muestra el mensaje de ayuda de argparse
        parser.print_help(sys.stderr)

        print(f'\n[!] Error: debes proporcionar los parámetreos requeridos\n')
        sys.exit(1)

    # # Analiza los argumentos introducidos por el usuario en la terminal y los devuelve como un objeto accesible
    return parser.parse_args()


# create tcp client
def tcp_client(server_ip, server_port):

    try:
        # Crea un socket TCP y asegura su cierre automático al finalizar el bloque
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            # Establece conexión con el servidor especificado por IP y puerto
            client.connect((server_ip,server_port))

            client.send(b"hola server")

            response = client.recv(4096)

            print(response)
    
    # Captura cualquier excepción en la conexión o transmisión e informa del error
    except Exception as e:
        print(f'error al conectar con el servidor: {e}')

        # finaliza el programa
        sys.exit(1)

def main():
     # Llama a la función de parseo de argumentos y almacena el resultado
    args = parse_arguments()

    tcp_client(args.ip, args.port)

# Comprueba si el script se está ejecutando directamente (no importado)
if __name__ == '__main__':
    main()
