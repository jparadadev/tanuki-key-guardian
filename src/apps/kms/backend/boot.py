from src.apps.kms.backend.KmsHttpServer import KmsHttpServer


def boot():
    server = KmsHttpServer()
    server.run()
