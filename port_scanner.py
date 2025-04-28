#!/usr/bin/python3

import argparse
import socket
import sys
import threading

def parse_arguments():
        parser = argparse.ArgumentParser(description="Port scanner",
        epilog="Example = python port_scanner.py 127.0.0.1"
        )
        parser.add_argument('target',type=str)

        if len(sys.argv) <= 1:
            parser.print_help(sys.stderr)
            print(f'\n [!] You have to provide the required parameters\n')
            sys.exit(1)
        return parser.parse_args()


def port_scann(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.setdefaulttimeout(0.5)
            result = s.connect_ex((target,port))
            if result == 0:
                 print(f'Port {port} open')
    except Exception as e:
        print(f'[!] Error connecting to the server: {e}')

def main():
    args = parse_arguments()
    for port in range(1,500):
        t = threading.Thread(target=port_scann, args=(args.target, port))
        t.start()

if __name__ == '__main__':
    main()