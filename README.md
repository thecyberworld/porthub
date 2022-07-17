# port-scanner
A fast port scanner written in python with a focus on reliability and simplicity. 

### Prerequisites
- [Python3](https://www.python.org/downloads/).

#### 🛠️ Installation Steps
1. Clone this project.
      
    `git clone https://github.com/thecyberworld/port-scanner.git`
2. Navigate to the project.
    
   `cd port-scanner`

#### Usage
Port specific:
- Syntax: `python3 scanner.py <ip> <port_start> <port_end>`

- Example: `python3 scanner.py 192.168.1.1 0 200`
![port_specific](https://user-images.githubusercontent.com/44284877/179356857-4676e09e-48ac-4cb8-96e3-2fa910a15e9a.gif)

Verbose mode:
- Syntax: `python3 scanner.py <ip> <port_start> <port_end> <verbose_mode> `

- Example: `python3 scanner.py 192.168.1.1 0 200 -v`
![Verbose mode](https://user-images.githubusercontent.com/44284877/179357933-76ef587a-9f74-4ab7-b466-164ca4fce445.gif)

