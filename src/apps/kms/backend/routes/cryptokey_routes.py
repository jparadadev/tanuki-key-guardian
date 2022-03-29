import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.kms.backend.controllers.KmsController import KmsController
from src.apps.kms.backend.dependencies.KmsContainer import KmsContainer, kms_container
from src.apps.kms.backend.dtos.crypto_key.CreateCryptoKeyCommandDto import \
    CreateCryptoKeyCommandDto


@inject
def register(
        router: APIRouter,
        cryptokeys_get_controller: KmsController = Provide[KmsContainer.cryptokeys_get_controller],
        cryptokeys_post_controller: KmsController = Provide[KmsContainer.cryptokeys_post_controller],
        rotate_cryptokey_put_controller: KmsController = Provide[KmsContainer.rotate_cryptokey_put_controller],
):
    @router.post('/cryptokeys', tags=["Crypto Keys"])
    async def run_wrapper(_: CreateCryptoKeyCommandDto, req: Request) -> JSONResponse:
        return await cryptokeys_post_controller.run(req)

    @router.get('/cryptokeys', tags=["Crypto Keys"])
    async def run_wrapper(req: Request) -> JSONResponse:
        return await cryptokeys_get_controller.run(req)

    @router.put('/cryptokeys/commands/rotate/{key_id}', tags=["Crypto Keys"])
    async def run_wrapper(key_id: str, req: Request) -> JSONResponse:
        return await rotate_cryptokey_put_controller.run(req)


kms_container.wire(modules=[sys.modules[__name__]])
