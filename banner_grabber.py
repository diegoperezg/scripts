import argparse
import socket
import sys
import threading

def parse_arguments():
    parser = argparse.ArgumentParser(description="Banner grabber",
    epilog="Example = python banner_grabber.py 127.0.0.1 -p 22 -o banners.txt"
    )

    parser.add_argument('target',type=str,help="IP addres of the target")
    parser.add_argument('-p','--port',type=int,default=1-500,help="Port of the service to get the banner")
    parser.add_argument('-o','--output',type=str,default="banners.txt",help="IP addres of the target")

    if len(sys.argv) <= 1:
        parser.print_help(sys.stderr)

        print(f'\n[!] Error: debes proporcionar los parámetreos requeridos\n')
        sys.exit(1)
    
    return parser.parse_args()


def banner(ip,port):
    try:
        with socket.socket() as s:
            s.settimeout(2.0)
            result = s.connect_ex((ip, port))
            if result == 0:
                banner = s.recv(1024).decode("utf-8")
                print(banner)

                args = parse_arguments()
                output_file = args.output
                if banner:
                        with open(output_file, "a") as f:
                            f.write(f"{args.target}:{args.port} - {banner}\n")
    
    except Exception as e:
        print(f"Error to connect to the server: {e}")


def main():
    args = parse_arguments()
    output_file = args.output


    t = threading.Thread(target=banner, args=(args.target, args.port))
    t.start()


if __name__ == '__main__':
    main()