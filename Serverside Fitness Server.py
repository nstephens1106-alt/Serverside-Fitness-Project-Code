import socket
from ClientHandler import ClientHandler

HOST = "localhost"
PORT = 9999
ADDRESS = (HOST, PORT)

def main():
    # Creates the server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binds the server address and listens
    server.bind(ADDRESS)
    server.listen()
    print(f"Sever Listening on {HOST}:{PORT}")

    #Accepts the client request via a loop
    while True:
        print("Waiting for client connection...")
        # Accepts a client connection 
        client_socket, client_address = server.accept()
        print(f"Connected with client {client_address}")

        # Passes off to handler
        handler = ClientHandler(client_socket)
        handler.start()

if __name__ == "__main__":
    main()