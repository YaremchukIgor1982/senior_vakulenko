from browsermobproxy import Server


class ProxyManager:
    _bmp = 'C:\\Users\Administrator\PycharmProjects\Scum\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat'

    def __init__(self):
        self.server = Server(ProxyManager._bmp)
        self.client = None

    def start_server(self):
        self.server.start()
        return self.server
    def start_client(self):
        self.client= self.server.create_proxy(params={"trustAllServers":"true"})
        return self.client


    # @property
    # def client(self):
    #     return self.client
    # @property
    # def server(self):
        self.server

