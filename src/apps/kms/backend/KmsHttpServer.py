import uvicorn

from src.apps.kms.backend.KmsFastApiApp import KmsFastApiApp
from src.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from src.contexts.shared.Infrastructure.environment.EnvVar import EnvVar


class KmsHttpServer:

    def __init__(self):
        self.app = KmsFastApiApp()

    def run(self):
        host = EnvManager.get(EnvVar.KMS_SERVER_HOST) or '0.0.0.0'
        port = EnvManager.get(EnvVar.KMS_SERVER_PORT, parser=int) or 80
        self.app.custom_openapi(host, port)
        uvicorn.run(self.app.get_runnable(), host=host, port=port)
