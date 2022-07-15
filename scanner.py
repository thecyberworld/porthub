#!/bin/python3

import sys
import socket
from datetime import datetime as time

# Define our target
target = ' '

if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    print("Example: python3 scanner.py 192.168.0.1")

# Pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(time.now()))
print("-" * 50)

try:
    for port in range(50, 85):  # 1, 65535
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port is {} open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting scanner.")
    sys.exit()

except socket.gaierror:
    print("Host name could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server/ip.")
    sys.exit()
