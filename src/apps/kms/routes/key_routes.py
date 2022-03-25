import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.backoffice.backend.controllers.CryptoKeyPostController import CryptoKeyPostController
from src.apps.backoffice.backend.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container
from src.apps.kms.controllers.KeyGeneratorGetController import KeyGeneratorGetController
from src.contexts.backoffice.cryptokeys.infrastructure.create_one.CreateCryptoKeyCommandDto import \
    CreateCryptoKeyCommandDto


@inject
def register(
        router: APIRouter
):
    @router.get('/keys', tags=["Simple Keys"])
    async def run_wrapper(algorithm: str, req: Request) -> JSONResponse:
        return await KeyGeneratorGetController().run(req)


backoffice_container.wire(modules=[sys.modules[__name__]])
