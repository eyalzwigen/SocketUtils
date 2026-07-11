import socket
import struct
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
    def __init__(self, server_info: ServerInfo):
        self.server_info = server_info
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def send_message(self, msg: str):
        """
        Sends a message to the client
        params:
            msg: The message (NOT ENCODED)
        """

        if not self.sock:
            raise ConnectionError("Socket not connected")

        header = struct.pack("!I", len(msg))
        data = msg.encode()
        self.sock.sendall(header + data)

    def _recv_exact(self, size: int):
        if not self.sock:
            raise ConnectionError("Socket not connected")

        data = bytearray()
        while len(data) < size:
            chunk = self.sock.recv(size - len(data))
            if not chunk:
                raise ConnectionError("Socket not connected")
            data.extend(chunk)

        return bytes(data)

    def listen_to_message(self) -> str:
        """
        Returns a message from the server
        """
        header = self._recv_exact(4)
        message_length = struct.unpack("!I", header)[0]

        message = self._recv_exact(message_length)
        return message.decode("utf-8")