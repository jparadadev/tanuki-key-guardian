from fastapi import FastAPI, APIRouter
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware

from src.apps.kms.backend.routes import register_routes


class KmsFastApiApp:

    def __init__(self):
        self._app: FastAPI = FastAPI()

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

    def custom_openapi(self, current_host=None, current_port=None):
        if self._app.openapi_schema:
            return self._app.openapi_schema
        openapi_schema = get_openapi(
            title="Tanuki Key Guardian - KMS",
            version="1.0.0",
            routes=self._app.routes,
            license_info={
                'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
                'name': 'Apache 2.0'
            }
        )
        servers = []
        if current_host and current_port:
            servers.append({
                'url': f'{current_host}:{current_port}',
                'description': 'Localhost'
            })

        # servers.extend([
        #     {
        #         'url': 'any_url.com',
        #         'description': 'static_sample'
        #     }
        # ])

        openapi_schema['servers'] = servers
        self._app.openapi_schema = openapi_schema
        return self._app.openapi_schema

    def get_runnable(self):
        return self._app
