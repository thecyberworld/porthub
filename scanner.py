import subprocess
import sys
import socket
from datetime import datetime
import os
from termcolor import colored
# Blank your screen
# subprocess.call('clear', shell=True)

try: 
    os.system("pip install -r req.txt")
except:
    pass
try: 
    os.system("cls||clear")
except: 
    pass
target = ' '  # Define our target
port_start = 0  # Default port range
port_end = 100
count = 0
open_ports = []
output_file_index = ' '
store_open_ports = ' '
banner = """

                                                                                                                               
                                                                                                                               
                                 ___                                                                                           
,-.----.                       ,--.'|_                                                                                         
\    /  \    ,---.    __  ,-.  |  | :,'     ,---,.                                        ,---,      ,---,             __  ,-. 
|   :    |  '   ,'\ ,' ,'/ /|  :  : ' :   ,'  .' | .--.--.                            ,-+-. /  | ,-+-. /  |          ,' ,'/ /| 
|   | .\ : /   /   |'  | |' |.;__,'  /  ,---.'   ,/  /    '     ,---.     ,--.--.    ,--.'|'   |,--.'|'   |   ,---.  '  | |' | 
.   : |: |.   ; ,. :|  |   ,'|  |   |   |   |    |  :  /`./    /     \   /       \  |   |  ,"' |   |  ,"' |  /     \ |  |   ,' 
|   |  \ :'   | |: :'  :  /  :__,'| :   :   :  .'|  :  ;_     /    / '  .--.  .-. | |   | /  | |   | /  | | /    /  |'  :  /   
|   : .  |'   | .; :|  | '     '  : |__ :   |.'   \  \    `. .    ' /    \__\/: . . |   | |  | |   | |  | |.    ' / ||  | '    
:     |`-'|   :    |;  : |     |  | '.'|`---'      `----.   \    ; :__   ," .--.; | |   | |  |/|   | |  |/ '   ;   /|;  : |    
:   : :    \   \  / |  , ;     ;  :    ;          /  /`--'  /'   | '.'| /  /  ,.  | |   | |--' |   | |--'  '   |  / ||  , ;    
|   | :     `----'   ---'      |  ,   /          '--'.     / |   :    :;  :   .'   \|   |/     |   |/      |   :    | ---'     
`---'.|                         ---`-'             `--'---'   \   \  / |  ,     .-./'---'      '---'        \   \  /           
  `---`                                                        `----'   `--`---'                             `----'  V0.5.1  
                                                                                                                                          
                            [::] Fast port scanner and easy to use! [::]
                           [::] Builded By: @thecyberworld and @VczZ0 [::]


"""

print(colored(banner, "green"))

help = """
]> Invalid amount of arguments <[
-----------------------------------------------------------------------------
Syntax: 
> python3 scanner.py <ip>
> python3 scanner.py <ip> -v
> python3 scanner.py <ip> -o <output_file>
> python3 scanner.py <ip> <port_start> <port_end>
> python3 scanner.py <ip> <port_start> <port_end> -o <output_file> -v
-----------------------------------------------------------------------------
Examples:
> python3 scanner.py thecyberhub.org
> python3 scanner.py 192.168.1.1
> python3 scanner.py 192.168.1.1 --host
> python3 scanner.py 192.168.1.1 --ip
> python3 scanner.py 192.168.1.1 -v
> python3 scanner.py 192.168.1.1 -o output.txt
> python3 scanner.py 192.168.1.1 -o output.txt -v
> python3 scanner.py 192.168.1.1 -p 50 150 -v
> python3 scanner.py 192.168.1.1 -p 50 150 -o output.txt
> python3 scanner.py 192.168.1.1 -p 50 150 -o output.txt -v
-----------------------------------------------------------------------------
"""

if len(sys.argv) == 1:
    print(colored(help, "red"))
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
banner_1 = f"""
-----------------------------------------------------------------------------
Target: {target}
Target IPv4: {target_ip}
Ports Range: {port_start}-{port_end}
Time started: {str(time1)[:-4]} 
-----------------------------------------------------------------------------\n
"""
print(colored(banner_1, "green"))


try:
    for port in range(port_start, port_end + 1):  # 1, 65535
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))

        if "-v" in sys.argv:
            if result == 0:
                print(colored("Port {}: open".format(port), "green"))
                count = count + 1
                open_ports.append(port)
            else:
                print(colored("Port {}: closed".format(port), "red"))

        else:
            if result == 0:
                if "--host" in sys.argv:
                    print(f"{target}: {port}")
                elif "--ip" in sys.argv:
                    print(f"{target_ip}: {port}")
                else:
                    print(colored(f"Port {port}: open", "green"))

                count = count + 1
                open_ports.append(port)

        if "-o" in sys.argv:
            if result == 0:
                store_open_ports.write(f"{target_ip}:" + str(port) + "\n")

        sock.close()
    
    print(colored("\n-----------------------------------------------------------------------------", "green"))
    if open_ports == []:
        print(colored("No open ports", "green"))
    else:
        print(colored("Open ports: {}".format(open_ports), "green"))
        print(colored("Total ports open: {}".format(count), "green")) 
    
except KeyboardInterrupt:
    print(colored("\nExiting scanner.", "red"))
    sys.exit()

except socket.gaierror:
    print(colored("Host name could not be resolved.", "red"))
    sys.exit()

except socket.error:
    print(colored("Could not connect to server/ip.", "red"))
    sys.exit()

if "-o" in sys.argv:
    print(colored(f"Output file: {output_file_index}", "green"))

# Checking the time again
time2 = datetime.now()
total_time_taken = time2 - time1
print(colored("Scanning completed in {} ".format(total_time_taken)[:-5], "green"))
print(colored("-----------------------------------------------------------------------------", "green"))
