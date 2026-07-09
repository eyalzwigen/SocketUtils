import socket
from SocketUtils.general import ServerInfo, SocketObject

class TCP_Server(SocketObject):
    def __init__(self, server_info: ServerInfo, max_bytes: int = 1024):
        super().__init__(max_bytes)

        self.server_info: ServerInfo = server_info
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc = None

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

    def send_message(self, msg: str):
        """
        Sends a message to the client and then returns the response
        params:
            msg: The message (NOT ENCODED)
        returns:
            The response of the client
        """
        if self.client_soc:
            self.client_soc.sendall(msg.encode())

    def listen_to_message(self) -> str | None:
        """
        Returns a message from the client
        """
        if self.client_soc:
            return self.client_soc.recv(self.max_bytes).decode()
        return None
