import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.backoffice.backend.controllers.CryptoKeyPostController import CryptoKeyPostController
from src.apps.backoffice.backend.controllers.CryptoKeysGetController import CryptoKeysGetController
from src.apps.backoffice.backend.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container
from src.contexts.backoffice.cryptokeys.infrastructure.create_one.CreateCryptoKeyCommandDto import \
    CreateCryptoKeyCommandDto


@inject
def register(
        router: APIRouter,
        cryptokeys_get_controller: CryptoKeysGetController = Provide[BackofficeContainer.cryptokeys_get_controller],
        cryptokeys_post_controller: CryptoKeyPostController = Provide[BackofficeContainer.cryptokeys_post_controller],
):
    @router.post('/cryptokeys', tags=["Crypto Keys"])
    async def run_wrapper(_: CreateCryptoKeyCommandDto, req: Request) -> JSONResponse:
        return await cryptokeys_post_controller.run(req)

    @router.get('/cryptokeys', tags=["Crypto Keys"])
    async def run_wrapper(req: Request) -> JSONResponse:
        return await cryptokeys_get_controller.run(req)


backoffice_container.wire(modules=[sys.modules[__name__]])
