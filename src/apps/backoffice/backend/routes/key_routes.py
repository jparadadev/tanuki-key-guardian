import sys

from dependency_injector.wiring import inject
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.backoffice.backend.dependencies.BackofficeContainer import backoffice_container
from src.apps.backoffice.backend.controllers.KeyGeneratorGetController import KeyGeneratorGetController


@inject
def register(
        router: APIRouter
):
    @router.get('/keys', tags=["Simple Keys"])
    async def run_wrapper(algorithm: str, req: Request) -> JSONResponse:
        return await KeyGeneratorGetController().run(req)


backoffice_container.wire(modules=[sys.modules[__name__]])
