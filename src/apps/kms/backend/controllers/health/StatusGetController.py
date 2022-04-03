from http import HTTPStatus

from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.kms.backend.controllers.KmsController import KmsController


class StatusGetController(KmsController):

    def __init__(self):
        pass

    async def run(self, req: Request) -> JSONResponse:
        return JSONResponse(status_code=HTTPStatus.OK)
