from src.apps.kms.KmsServer import KmsServer


def boot():
    server = KmsServer()
    server.run()
