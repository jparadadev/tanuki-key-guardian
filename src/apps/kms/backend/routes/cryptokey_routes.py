import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.kms.backend.controllers.CryptoKeyPostController import CryptoKeyPostController
from src.apps.kms.backend.controllers.CryptoKeysGetController import CryptoKeysGetController
from src.apps.kms.backend.dependencies.KmsContainer import KmsContainer, kms_container
from src.contexts.kms.cryptokeys.infrastructure.create_one.CreateCryptoKeyCommandDto import \
    CreateCryptoKeyCommandDto


@inject
def register(
        router: APIRouter,
        cryptokeys_get_controller: CryptoKeysGetController = Provide[KmsContainer.cryptokeys_get_controller],
        cryptokeys_post_controller: CryptoKeyPostController = Provide[KmsContainer.cryptokeys_post_controller],
):
    @router.post('/cryptokeys', tags=["Crypto Keys"])
    async def run_wrapper(_: CreateCryptoKeyCommandDto, req: Request) -> JSONResponse:
        return await cryptokeys_post_controller.run(req)

    @router.get('/cryptokeys', tags=["Crypto Keys"])
    async def run_wrapper(req: Request) -> JSONResponse:
        return await cryptokeys_get_controller.run(req)


kms_container.wire(modules=[sys.modules[__name__]])
