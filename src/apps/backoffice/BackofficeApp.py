from fastapi import FastAPI, APIRouter

from src.apps.backoffice.routes import register_routes


class BackofficeApp:

    def __init__(self):
        self._app: FastAPI = FastAPI()
        router: APIRouter = APIRouter()
        register_routes(router)
        self._app.include_router(router, prefix='/api')

    def get_runnable(self):
        return self._app
