import socket

HOST = "localhost"
PORT = 9999
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

def main():
    try:
        # Creates socket and connects to server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDRESS)

        clinet_handler_init_message = client.recv(BUFSIZE).decode()
        print(clinet_handler_init_message)

        while True:
            server_prompt = client.recv(BUFSIZE).decode()
            if not server_prompt:
                break
            print(server_prompt)
            user_input = input("> ")
            client.send(user_input.encode())

    except ConnectionRefusedError:
        print("Error connecting to the server.")
    finally:
        client.close()

if __name__ == "__main__":
    main()