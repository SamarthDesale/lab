# Experiment No. 4: Inter-Process Communication (Client Program)
import socket

HOST = "127.0.0.1"  # localhost
PORT = 6666


def start_client() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        a = int(input("Enter 1st no:\n"))
        b = int(input("Enter 2nd no:\n"))

        client_socket.sendall(f"{a},{b}".encode("utf-8"))
        print("Numbers sent to server.")


if __name__ == "__main__":
    try:
        start_client()
    except ConnectionRefusedError:
        print("Connection failed: Start server.py first.")
    except ValueError:
        print("Invalid input: Enter integer numbers only.")
    except Exception as err:
        print(f"Client error: {err}")


# Experiment No. 4: Inter-Process Communication (Server Program)
import socket

HOST = "127.0.0.1"  # localhost
PORT = 6666


def start_server() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected to client: {addr}")
            data = conn.recv(1024).decode("utf-8").strip()
            if data:
                a, b = map(int, data.split(","))
                print(f"Received: {a}, {b}")
                print(f"Sum = {a + b}")


if __name__ == "__main__":
    try:
        start_server()
    except Exception as err:
        print(f"Server error: {err}")