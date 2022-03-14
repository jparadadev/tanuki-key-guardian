from src.apps.keyhub.KeyhubServer import KeyhubServer


def boot():
    server = KeyhubServer()
    server.run()
