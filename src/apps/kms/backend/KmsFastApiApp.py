from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from src.apps.kms.backend.routes import register_routes


class KmsFastApiApp:

    def __init__(self):
        self._app: FastAPI = FastAPI(
            title="Tanuki Key Guardian - KMS",
            license_info={
                'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
                'name': 'Apache 2.0'
            }
        )

        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        router: APIRouter = APIRouter()
        register_routes(router)
        self._app.include_router(router, prefix='/api')

    def get_runnable(self):
        return self._app
