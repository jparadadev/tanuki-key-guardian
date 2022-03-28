import sys

from dependency_injector.wiring import inject
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.kms.backend.dependencies.KmsContainer import kms_container
from src.apps.kms.backend.controllers.KeyGeneratorGetController import KeyGeneratorGetController


@inject
def register(
        router: APIRouter
):
    @router.get('/keys', tags=["Simple Keys"])
    async def run_wrapper(algorithm: str, req: Request) -> JSONResponse:
        return await KeyGeneratorGetController().run(req)


kms_container.wire(modules=[sys.modules[__name__]])
