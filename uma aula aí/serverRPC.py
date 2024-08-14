import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass
    def exposed_add_numbers(self, x, y):
        return x+y

if __name__=="__main__":
    from rypc.utils.server import threadedServer
    server = threadedServer(MyService, port=12345)
    server.start()