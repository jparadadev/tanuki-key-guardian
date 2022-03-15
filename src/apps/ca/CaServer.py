import uvicorn

from src.apps.ca.CaApp import CaApp
from src.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from src.contexts.shared.Infrastructure.environment.EnvVar import EnvVar


class CaServer:

    def __init__(self):
        self.app = CaApp()

    def run(self):
        host = EnvManager.get(EnvVar.BACKOFFICE_SERVER_HOST)
        port = EnvManager.get(EnvVar.BACKOFFICE_SERVER_PORT, parser=int)
        uvicorn.run(self.app.get_runnable(), host=host, port=port)
