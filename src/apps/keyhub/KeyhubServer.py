import uvicorn

from src.apps.backoffice.backend.BackofficeApp import BackofficeApp
from src.apps.keyhub.KeyhubApp import KeyhubApp
from src.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from src.contexts.shared.Infrastructure.environment.EnvVar import EnvVar


class KeyhubServer:

    def __init__(self):
        self.app = KeyhubApp()

    def run(self):
        host = EnvManager.get(EnvVar.BACKOFFICE_SERVER_HOST)
        port = EnvManager.get(EnvVar.BACKOFFICE_SERVER_PORT, parser=int)
        uvicorn.run(self.app.get_runnable(), host=host, port=port)
