import socket

HOST = '127.0.0.1'
PORT = 50007

def send_message(sock, message):
    try:
        sock.send(message.encode('utf-8'))
        print(f"Sent: {message}")
    except:
        print("Error sending message")

def receive_message(sock):
    try:
        data = sock.recv(1024)
        if data:
            print(f"Received: {data.decode('utf-8')}")
        else:
            print("Disconnected from server")
            sock.close()
    except:
        print("Error receiving message")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((HOST, PORT))
        print(f"Connected to server {HOST}:{PORT}")

        while True:
            message = input("Enter message (press Enter to send): ")
            if not message:
                continue
            send_message(s, message)
            receive_message(s)
    except ConnectionRefusedError:
        print(f"Connection to {HOST}:{PORT} refused")
    except:
        print("An error occurred")

    s.close()

if __name__ == "__main__":
    main()
