import socket
from general import ServerInfo, SocketObject

class TCP_Client(SocketObject):
    def __init__(self, server_info: ServerInfo, max_bytes: int = 1024):
        super().__init__(max_bytes)

        self.sock = None
        self.server_info = server_info

    def get_server_info(self):
        return self.server_info.get_info()

    def set_server_info(self, server_info: ServerInfo):
        self.server_info = server_info

    def connect(self):
        """
        Connect To Server
        """
        address = self.get_server_info()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(address)

    def disconnect(self):
        """
        Disconnect from server
        """
        if self.sock:
            self.sock.close()
            self.sock = None

    def get_socket(self):
        return self.sock

    def send_message(self, msg: str):
        """
        Sends a message to the server and then returns the response
        params:
            msg: The message (NOT ENCODED)
        returns:
            The response of the server
        """

        self.sock.sendall(msg.encode())

    def listen_to_message(self) -> str:
        """
        Returns a message from the server
        """

        return self.sock.recv(self.max_bytes).decode()