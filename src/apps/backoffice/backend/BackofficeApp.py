from fastapi import FastAPI, APIRouter

from src.apps.backoffice.backend.routes import register_routes


class BackofficeApp:

    def __init__(self):
        self._app: FastAPI = FastAPI(
            title="Tanuki Key Guardian - Backoffice",
            license_info={'url': 'https://www.apache.org/licenses/LICENSE-2.0.html', 'name': 'Apache 2.0'}
        )
        router: APIRouter = APIRouter()
        register_routes(router)
        self._app.include_router(router, prefix='/api')

    def get_runnable(self):
        return self._app
