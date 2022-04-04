import random
import socket
import time


def main():
    with socket.socket() as client:
        address = ('127.0.0.1', 2222)
        client.connect(address)
        print(f'Connected to {address[0]}:{address[1]}')
        while True:
            request = str(random.randrange(10))
            client.sendall(request.encode())
            response = client.recv(1024)
            if not response:
                break
            response = response.decode()
            print(f'{request} {response}')
            time.sleep(1)


if __name__ == '__main__':
    main()
