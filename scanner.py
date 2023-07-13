#!/bin/python3
import sys
import socket
import argparse
import subprocess
from termcolor import colored, cprint
from datetime import datetime as dt

# clear your terminal
# subprocess.call('clear', shell=True)

def exit() -> None:
    sys.exit()

def usage() -> None:
    print(colored(f"""
    => Usage <=
    {"-"*50}
    Syntax:
    > python scanner_v2.py --host <HostIP>
    > python scanner_v2.py --host <HostIP> -v
    > python scanner_v2.py --host <HostIP> -o <outputFileName>
    > python scanner_v2.py --host <HostIP> -p <portStart>-<portEnd>
    > python scanner_v2.py --host <HostIP> -p <portStart>-<portEnd> -v -o <outputFileName>
    {"-"*50}
    """, 'green'))
    exit()

def get_arguments():
    parser = argparse.ArgumentParser(description="Get arguments for port scanner")
    parser.add_argument("--host", dest="HOST", help="IP address of host machine")
    parser.add_argument('-o', '--output', dest='OUTPUT', help="Write the output into a file")
    parser.add_argument('-p', '--port', dest='PORTS', help="ports to scan, input in the form <start>-<end>", default="FULL")
    # parser.add_argument('-v', '--verbose', default='VERBOSE', help="increase output verbosity", action="store_true")
    args = parser.parse_args()
    if not args.HOST:
        print(colored(f"HOST IP address is required.", 'red'))
        usage()
    return args

target = ""
port_start, port_end, count = 0, 100, 0 #default data
open_ports = []
output_file = None
store_open_ports = ''

def display_conf_data() -> None:
    print("-" * 50)
    print("Scanning host(IPv4) -> " + target)
    # print("Target Ipv4: " + target)
    print(f"Ports Range: {port_start}-{port_end}")
    print(f"Output file: {output_file}")
    print("-" * 50)

def find_open_ports():
    try:
        for port in range(port_start, port_end+1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                if output_file:
                    store_open_ports.write(f"{target}:{port} => OPEN\n")
                print(f"{target}:{port} => OPEN")
                open_ports.append(port)
                global count
                count = count + 1
            else:
                print(f"{target}:{port} => CLOSED")
            
            sock.close()
        
        print(f'''
{"-"*50}
Total Open Ports: {count}
Open Ports: {open_ports}
        ''')

    except KeyboardInterrupt:
        print(colored("\n <- Keyboard Interruption - Terminating scan ->", "red"))
        exit()
    except socket.gaierror:
        print(colored(" !Host name could not be resolved! ", "red"))
        exit()
    except socket.error:
        print(colored(f" !Could not connect to host/ip {target} ", "red"))
        exit()

if __name__ == '__main__':
    start_time = dt.now()
    print("Time started: " + str(start_time))
    args = get_arguments()
    target = args.HOST
    ports = args.PORTS
    if "-" in ports:
        port_start, port_end = ports.split("-")
        port_start = int(port_start)
        port_end = int(port_end)
    elif ports == "FULL": #complete port scan
        port_start, port_end = 1, 65535
    else:
        port_start = int(ports) or port_start
    # check the start and end port values, if they are in same order or not
    if port_start > port_end:
        port_start, port_end = port_end, port_start
    
    if args.OUTPUT:
        output_file = args.OUTPUT
        store_open_ports = open(f"{output_file}", "a")

    display_conf_data()
    find_open_ports()

    end_time = dt.now()
    total_time = end_time - start_time
    print(f"Scanning completed in {total_time}")
    print("="*35)
    exit()
