import socket
from datetime import datetime

def port_scanner(target_ip, start_range, end_range):
    try:
        for port in range(start_range, end_range + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port} is OPEN")
                else:
                    print(f"Port {port} is closed")
    except socket.error as e:
        print(f"Could not connect to target: {e}")
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")

if __name__ == "__main__":
    target_ip = input("Enter the target IP for scanning: ")
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))

    start_time = datetime.now()
    port_scanner(target_ip, start_range, end_range)
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Your scan finished in: {total_time}")
