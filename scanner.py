#!/bin/python3
import subprocess
import sys
import socket
from datetime import datetime

# Blank your screen
# subprocess.call('clear', shell=True)

target = ' '  # Define our target
port_start = 0  # Default port range
port_end = 100
count = 0
open_ports = []
output_file_index = ' '
store_open_ports = ' '

if len(sys.argv) == 1:
    print(" ")
    print("]}> Invalid amount of arguments <{[")
    print("-" * 50)
    print("Syntax: ")
    print("> python3 scanner.py <ip>")
    print("> python3 scanner.py <ip> -v")
    print("> python3 scanner.py <ip> -o <output_file>")
    print("> python3 scanner.py <ip> <port_start> <port_end>")
    print("> python3 scanner.py <ip> <port_start> <port_end> -o <output_file> -v")
    print("-" * 50)

    print("Examples:")
    print("> python3 scanner.py thecyberhub.org")
    print("> python3 scanner.py 192.168.1.1")
    print("> python3 scanner.py 192.168.1.1 --host")
    print("> python3 scanner.py 192.168.1.1 --ip")
    print("> python3 scanner.py 192.168.1.1 -v")
    print("> python3 scanner.py 192.168.1.1 -o output.txt")
    print("> python3 scanner.py 192.168.1.1 -o output.txt -v")
    print("> python3 scanner.py 192.168.1.1 -p 50 150 -v")
    print("> python3 scanner.py 192.168.1.1 -p 50 150 -o output.txt")
    print("> python3 scanner.py 192.168.1.1 -p 50 150 -o output.txt -v")
    print("-" * 50)
    sys.exit()

else:
    # Translate hostname to IPv4
    target = sys.argv[1]
    target_ip = socket.gethostbyname(sys.argv[1])

    for i in range(0, len(sys.argv)):
        if "-p" == sys.argv[i]:
            port_start = int(sys.argv[i + 1])
            port_end = int(sys.argv[i + 2])

        if "-o" == sys.argv[i]:
            output_file_index = sys.argv[i + 1]
            store_open_ports = open(f"{output_file_index}", "a")

# Check the date and time the scan was started.
time1 = datetime.now()

# Pretty banner
print("""                                                                        
                                   .@@@@@@@@@                                   
    Port-Scanner               (@@@@@@@@@@@@@@@@@,                              
               @@@@@@@@&     @@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@              
          @@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@#   @@@@@@@@@@@@@@@@@@@         
       @@@@@@@@@@@@@@@@@@@@@@@@%  (@@@@@@@@@@@.  @@@@@@@@@@@@@@@@@@@@@@@@@      
     #@@@@@@@            /@@@@@@@   @@@@@@@@@  .@@@@@@@.           .@@@@@@@,    
    @@@@@@@  @@@%           @@@@@@#  @@@@@@@  @@@@@@@           @@@@  @@@@@@@   
   .@@@@@@  @@               @@@@@@  (@@@@@   @@@@@@               @@  @@@@@@   
   @@@@@@  @@                .@@@@@%  @@@@@  @@@@@@                 @@  @@@@@@  
   @@@@@@   @                %@@@@@* ,@@@@@  &@@@@@,                @  .@@@@@@  
    @@@@@@                   @@@@@@  @@@@@@@  @@@@@@                   @@@@@@   
     @@@@@@@               @@@@@@@  @@@@@@@@@  @@@@@@@               @@@@@@@    
      @@@@@@@@@         @@@@@@@@@               @@@@@@@@@         @@@@@@@@@     
        @@@@@@@@@@@@@@@@@@@@@@@                   @@@@@@@@@@@@@@@@@@@@@@@       
           (@@@@@@@@@@@@@@@.                         ,@@@@@@@@@@@@@@@,          
          """)
print("-" * 35)
print("Target: " + target)
print("Target Ipv4: " + target_ip)
print(f"Ports Range: {port_start}-{port_end}")
print("Time started: " + str(time1))
print("-" * 35)

try:
    for port in range(port_start, port_end + 1):  # 1, 65535
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))

        if "-v" in sys.argv:
            if result == 0:
                print("Port {}: open".format(port))
                count = count + 1
                open_ports.append(port)
            else:
                print("Port {}: close".format(port))

        else:
            if result == 0:
                if "--host" in sys.argv:
                    print(f"{target}: {port}")
                elif "--ip" in sys.argv:
                    print(f"{target_ip}: {port}")
                else:
                    print(f"Port {port}: open")

                count = count + 1
                open_ports.append(port)

        if "-o" in sys.argv:
            if result == 0:
                store_open_ports.write(f"{target_ip}:" + str(port) + "\n")

        sock.close()

    print("-" * 35)
    print("Open ports: {}".format(open_ports))
    print("Total ports open: {}".format(count))

except KeyboardInterrupt:
    print("\nExiting scanner.")
    sys.exit()

except socket.gaierror:
    print("Host name could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server/ip.")
    sys.exit()

if "-o" in sys.argv:
    print(f"Output file: {output_file_index}")

# Checking the time again
time2 = datetime.now()
total_time_taken = time2 - time1
print("Scanning completed in {} ".format(total_time_taken))
print("-" * 35)
