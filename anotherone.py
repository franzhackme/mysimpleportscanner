import socket
from ipaddress import ip_address


def scanner(ip, start_port, stop_port):
    for port in range(start_port, stop_port +1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((ip, port))
        except socket.timeout:
            print(f"The port {port} has timed out")
        except socket.error as err:
            print(f"The port {port} has run into a problem {err}")
        else:
            print(f"The port {port} is open.")

def main():
    ip = input("What is the target ip: ")
    try:
        ip_address(ip)
    except ValueError:
        print("Invalid ip address")
        return

    try:
        start_port = int(input("Please put in the first port: "))
        stop_port = int(input("Please put in the final port: "))
    except ValueError:
        print("Port numbers should be integers")
        return

    if start_port < 1 or stop_port > 65535:
        print("The port numbers should be between 1 and 65535")
        if start_port <= 1:
            print("Invalid range")
            if start_port > stop_port:
                print("The final port should be greater than the initial port.")
    return

    scanner(ip, start_port, stop_port)

if __name__ == "__main__":
    main()

