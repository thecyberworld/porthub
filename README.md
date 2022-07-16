# port-scanner
A fast port scanner written in python with a focus on reliability and simplicity. 

#### 🛠️ Installation Steps
1. Install python3.
2. Install git.
3. Clone this project.
    `git clone https://github.com/thecyberworld/port-scanner.git`
   or skip the step 2 and 3 by Download ZIP. 
4. Navigate to the project directory.

#### Usage
Port specific:
- Syntax: `python3 scanner.py <ip> <port_start> <port_end>`

- Example: `python3 scanner.py 192.168.1.1 0 200`
![port_specific](https://user-images.githubusercontent.com/44284877/179356857-4676e09e-48ac-4cb8-96e3-2fa910a15e9a.gif)

Verbose mode:
- Syntax: `python3 scanner.py <ip> <port_start> <port_end> <verbose_mode> `

- Example: `python3 scanner.py 192.168.1.1 0 200 -v`
![Verbose mode](https://user-images.githubusercontent.com/44284877/179357933-76ef587a-9f74-4ab7-b466-164ca4fce445.gif)

