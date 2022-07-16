#!/bin/python3
import subprocess
import sys
import socket
from datetime import datetime

# Blank your screen
# subprocess.call('clear', shell=True)

# Define our target
target = ' '
port_start = ' '
port_end = ' '
count = 0
open_ports = []

# default settings
if len(sys.argv) == 2 or len(sys.argv) == 3:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
    port_start = 0
    port_end = 1000

elif len(sys.argv) == 4 or len(sys.argv) == 5:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
    port_start = int(sys.argv[2])
    port_end = int(sys.argv[3])

else:
    print("Invalid amount of arguments.")
    print("-" * 50)

    print("Syntax")
    print("> python3 scanner.py <ip>")
    print("> python3 scanner.py <ip> -v")
    print("> python3 scanner.py <ip> <port_start> <port_end>")
    print("> python3 scanner.py <ip> <port_start> <port_end> -v")
    print("-" * 50)

    print("Examples:")
    print("> python3 scanner.py 192.168.0.1")
    print("> python3 scanner.py 192.168.0.1 -v")
    print("> python3 scanner.py 192.168.0.1 150 1333")
    print("> python3 scanner.py 192.168.0.1 150 1333 -v")
    print("-" * 50)

    sys.exit()

    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip> <start_port> <last_port>")
    print("Example: python3 scanner.py 192.168.0.1 0 8888")
    sys.exit()

# Check the date and time the scan was started.
time1 = datetime.now()

# Pretty banner
print("-" * 35)
print("Target: " + target)
if len(sys.argv) == 2 or len(sys.argv) == 3:
    print("Default range: {}-{}".format(port_start, port_end))
else:
    print("Ports Range: {}-{}".format(port_start, port_end))
print("Time started: " + str(time1))
print("-" * 35)

try:
    for port in range(port_start, port_end + 1):  # 1, 65535
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if "-v" in sys.argv:
            if result == 0:
                print("Port {}: open".format(port))
                count = count + 1
                open_ports.append(port)

            else:
                print("Port {}: close".format(port))
        else:
            if result == 0:
                print("Port {}: open".format(port))
                count = count + 1
                open_ports.append(port)

        sock.close()

    print("-" * 35)
    print("Open ports: {}".format(open_ports))
    print("Total open ports: {}".format(count))

except KeyboardInterrupt:
    print("\nExiting scanner.")
    sys.exit()

except socket.gaierror:
    print("Host name could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server/ip.")
    sys.exit()

# Checking the time again
time2 = datetime.now()

total_time_taken = time2 - time1
print("Scanning completed in {} ".format(total_time_taken))
print("-" * 35)
