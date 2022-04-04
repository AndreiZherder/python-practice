import socket


def run_server(port: int):
    with socket.socket() as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('', port))
        server.listen()
        serve(server)


def serve(server: socket.socket):
    accept_connection(server)


def accept_connection(server: socket.socket):
    while True:
        client, addr = server.accept()
        print(f'Connected by {client.getpeername()}')
        serve_client(client)


def serve_client(client: socket.socket):
    with client:
        while True:
            request = read_request(client)
            if not request:
                print(f'{client.getpeername()} disconnected')
                break
            response = handle_request(request)
            write_response(client, response)


def read_request(client: socket.socket) -> bytes:
    request = client.recv(1024)
    return request


def handle_request(request: bytes) -> bytes:
    return str(int(request.decode()) * 2).encode()


def write_response(client: socket.socket, response: bytes):
    client.sendall(response)


def main():
    run_server(2222)


if __name__ == '__main__':
    main()
