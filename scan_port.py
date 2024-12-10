import socket

def port_scanner(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")
    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
    except KeyboardInterrupt:
        print("\nScan terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("\nScan complete.")

if __name__ == "__main__":

    print()
    print("Tools     : Port Scanner ")
    print("Author    : MR_4WP ")
    print("Community : ANONYMOUS WEST PAPUA ")
    print("................................")
    print()
    print()

    target = input("Enter target IP address (192.168.1.1) : ")
    start = int(input("Enter the starting port number (1) : "))
    end = int(input("Enter the ending port number (65535) : "))

    if start > 0 and end <= 65535 and start <= end:
        port_scanner(target, start, end)
    else:
        print("Invalid port range. Please enter valid port numbers between 1 and 65535.")
