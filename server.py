import socket
import threading
import signal
import sys

HOST = '127.0.0.1'
PORT = 50007

def handle_client(conn, addr):
    print(f"Connected client: {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print(f"Client {addr} disconnected")
                break
            else:
                print(f"Received from {addr}: {data.decode()}")
                conn.send(data)
                print(f"Sent to {addr}: {data.decode()}")
        except ConnectionResetError:
            print(f"Client {addr} forcibly disconnected")
            break
        except:
            print(f"An error occurred with client {addr}")
            break
    conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)  # Allow up to 5 queued connections

    print(f"Server listening on {HOST}:{PORT}")

    def signal_handler(sig, frame):
        print("Exiting server...")
        s.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)  # Register Ctrl+C signal handler

    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
