import socket
import struct
from SocketUtils.general import ServerInfo, SocketObject

class TCP_Client(SocketObject):
    def __init__(self, server_info: ServerInfo, max_bytes: int = 1024):
        super().__init__(server_info)

    def get_server_info(self):
        return self.server_info.get_info()

    def set_server_info(self, server_info: ServerInfo):
        self.server_info = server_info

    def connect(self):
        """
        Connect To Server
        """
        address = self.get_server_info()
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

