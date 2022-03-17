from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.ca.controllers.CaController import CaController


class StatusGetController(CaController):

    def __init__(self):
        pass

    async def run(self, req: Request) -> JSONResponse:
        return JSONResponse(status_code=HTTPStatus.OK)
