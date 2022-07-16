#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target
target = ' '

if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    print("Example: python3 scanner.py 192.168.0.1")


# Check the date and time the scan was started.
time1 = datetime.now()

# Pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(time1))
print("-" * 50)

try:
    for port in range(50, 85):  # 1, 65535
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print("Port {}:   open".format(port))
        sock.close()

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
