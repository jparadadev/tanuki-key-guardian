import uvicorn

from src.apps.kms.backend.KmsFastApiApp import KmsFastApiApp
from src.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from src.contexts.shared.Infrastructure.environment.EnvVar import EnvVar


class KmsHttpServer:

    def __init__(self):
        self.app = KmsFastApiApp()

    def run(self):
        host = EnvManager.get(EnvVar.BACKOFFICE_SERVER_HOST)
        port = EnvManager.get(EnvVar.BACKOFFICE_SERVER_PORT, parser=int)
        uvicorn.run(self.app.get_runnable(), host=host, port=port)