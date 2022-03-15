from src.apps.ca.CaServer import CaServer


def boot():
    server = CaServer()
    server.run()
