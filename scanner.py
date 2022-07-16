#!/bin/python3
import subprocess
import sys
import socket
from datetime import datetime

# Blank your screen
# subprocess.call('clear', shell=True)

# Define our target
target = ' '
start_port = ' '
last_post = ' '
count = 0
open_ports = []

if len(sys.argv) == 4 or 5:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
    start_port = int(sys.argv[2])
    last_post = int(sys.argv[3])

else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip> <start_port> <last_port>")
    print("Example: python3 scanner.py 192.168.0.1 0 8888")

# Check the date and time the scan was started.
time1 = datetime.now()

# Pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(time1))
print("-" * 50)

try:
    for port in range(start_port, last_post):  # 1, 65535
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

    print("-" * 50)
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
