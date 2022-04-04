import heapq
import selectors
import socket
import time


class Loop:
    def __init__(self):
        self.tasks = []
        self.task_id = 0
        self.selector = selectors.DefaultSelector()

    def create_task(self, start_time: float, task):
        heapq.heappush(self.tasks, (start_time, self.task_id, task))
        self.task_id += 1

    def run(self):
        while self.tasks:
            start_time, task_id, task = heapq.heappop(self.tasks)
            wait = start_time - time.time()
            if wait > 0:
                time.sleep(wait)
            try:
                delay, fileobj, events = task.send(None)
            except StopIteration:
                continue
            if fileobj:
                self.selector.register(fileobj, events, (task_id, task))
            else:
                heapq.heappush(self.tasks, (time.time() + delay, task_id, task))
            if self.selector.get_map():
                for key, events in self.selector.select(timeout=0):
                    print(key, events)
                    self.selector.unregister(key.fileobj)
                    task_id = key.data[0]
                    task = key.data[1]
                    heapq.heappush(self.tasks, (time.time(), task_id, task))


loop = Loop()


def run_server(port: int):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(False)
    server.bind(('', port))
    server.listen()
    loop.create_task(time.time(), accept_connection(server))


def accept_connection(server: socket.socket):
    with server:
        while True:
            yield 0, server, selectors.EVENT_READ
            client, addr = server.accept()
            print(f'Connected by {client.getpeername()}')
            client.setblocking(False)
            loop.create_task(time.time(), serve_client(client))


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
    yield 0, client, selectors.EVENT_READ
    request = client.recv(1024)
    return request


def handle_request(request: bytes) -> bytes:
    return str(int(request.decode()) * 2).encode()


def write_response(client: socket.socket, response: bytes):
    yield 0, client, selectors.EVENT_WRITE
    client.sendall(response)


def clock():
    print(time.strftime("%H:%M:%S", time.localtime()))
    while True:
        yield 1, None, None
        print(time.strftime("%H:%M:%S", time.localtime()))


def bang():
    print('Bang')
    while True:
        yield 3, None, None
        print('Bang')


def main():
    loop.create_task(time.time(), bang())
    loop.create_task(time.time(), clock())
    run_server(2222)
    loop.run()


if __name__ == '__main__':
    main()
