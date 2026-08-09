import socket


def scan_port(host, port):
    """
    Check whether a TCP port is open.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    sock.close()


def main():
    print("=== Simple Port Scanner ===")

    host = input("Enter IP address or hostname: ")

    ports = [22, 80, 443, 3306]

    print(f"\nScanning {host}...\n")

    for port in ports:
        scan_port(host, port)


if __name__ == "__main__":
    main()