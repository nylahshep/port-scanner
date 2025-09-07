import socket 

target = input("Enter a domain or IP: ")
ip = socket.gethostbyname(target)

print(f"\nScanning target: {target}({ip})\n")

open_ports = []
for port in range(1,101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)
    s.close()


