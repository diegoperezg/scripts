import argparse
import socket
import threading
import sys

def parse_arguments():

    # parameters to get ip and port
    parser = argparse.ArgumentParser(description="Start listening to receive connections", add_help=False,
    epilog="Example = python tcp_server.py 127.0.0.1 7777")
    
    parser.add_argument('-h','--host', type=str, help="IP to be listening", default="0.0.0.0")
    parser.add_argument('-p','--port', type=int, help="Port to be listening",default=8080)
    
    args = parser.parse_args()
    return args

# server tcp

def server_tcp(ip,port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

            server.bind((ip,port))

            server.listen(3)

            print(f'listening on {ip}:{port}')

            while True:

                client, address = server.accept()

                print(f'accepted connection from {address[0]}')

                client_handler = threading.Thread(target=handle_client, args=(client,))

                client_handler.start()
    
    except Exception as e:
        print(f'Error al conectar con el servidor: {e}')
        sys.exit(1)

    except socket.error as e:
        print(f'error de socket: {e}')
        sys.exit(1)

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'{request.decode("utf-8")}')
        sock.send(b'resposta')

def main():
    args = parse_arguments()
    server_tcp(args.host,args.port)


if __name__ == '__main__':
    main()