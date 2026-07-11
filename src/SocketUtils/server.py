import socket
import struct
from SocketUtils.general import ServerInfo, SocketObject

class TCP_Server(SocketObject):
    def __init__(self, server_info: ServerInfo):
        super().__init__(server_info)

        self.server_info: ServerInfo = server_info
        self.listen_sock = self.sock
        self.client_soc = None

    def get_info(self) -> ServerInfo:
        return self.server_info
    def start_listener(self):
        """
        Start listening socket
        """
        self.listen_sock.bind(self.server_info.get_info())

        self.listen_sock.listen(1)

        self.client_soc, _ = self.listen_sock.accept()

    def close_listener(self):
        """
        Close listener socket
        """
        self.listen_sock.close()

    def close_server(self):
        """
        Close listener socket + client socket
        """
        self.close_listener()
        if self.client_soc:
            self.client_soc.close()

