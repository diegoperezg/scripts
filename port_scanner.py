#!/usr/bin/python3

import argparse
import socket
import sys
import threading

# function to parse arguments
def parse_arguments():
        # creating the parse
        parser = argparse.ArgumentParser(description="Port scanner",
        epilog="Example = python port_scanner.py 127.0.0.1"
        )
        parser.add_argument('target',type=str)

        # If no arguments are provided, show the help menu and exit
        if len(sys.argv) <= 1:
            parser.print_help(sys.stderr)
            print(f'\n [!] You have to provide the required parameters\n')
            sys.exit(1)
        return parser.parse_args()

# Function to scan a single port on the target host
def port_scann(target, port):
    try:
        # Using 'with' ensures the socket is closed automatically
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout of 0.5 seconds for the connection attempt
            socket.setdefaulttimeout(0.5)
            # connect_ex returns 0 if the connection succeeds (port is open)
            result = s.connect_ex((target,port))
            if result == 0:
                 print(f'Port {port} open')
    except Exception as e:
        print(f'[!] Error connecting to the server: {e}')

def main():
    # Store the parsed arguments in 'args'
    args = parse_arguments()
    # Loop through ports from 1 to 499
    for port in range(1,500):
        # Create a new thread to run port_scann with the required arguments
        t = threading.Thread(target=port_scann, args=(args.target, port))
        # Start the thread
        t.start()

if __name__ == '__main__':
    main()
