from server import Server
if __name__=="__main__":
    server = Server()
    try:
        server.serve()
    except KeyboardInterrupt:
        server.stop_serving()