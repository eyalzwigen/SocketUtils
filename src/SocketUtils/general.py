class ServerInfo:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.server_info = (address, port)

    def set_address(self, address: str):
        self.address = address
        self.server_info = (address, self.port)

    def set_port(self, port: int):
        self.port = port
        self.server_info = (self.address, port)

    def get_address(self):
        return self.address

    def get_port(self):
        return self.port

    def get_info(self):
        return self.server_info


class SocketObject:
    def __init__(self, max_bytes):
        self.max_bytes = max_bytes

    def get_max_bytes(self):
        return self.max_bytes

    def set_max_bytes(self, max_bytes):
        self.max_bytes = max_bytes