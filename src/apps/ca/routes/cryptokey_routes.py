import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.ca.controllers.CryptoKeysGetController import CryptoKeysGetController
from src.apps.ca.dependencies.CaContainer import CaContainer, ca_container


@inject
def register(
        router: APIRouter,
        cryptokeys_get_controller: CryptoKeysGetController = Provide[CaContainer.cryptokeys_get_controller],
):
    @router.get('/cryptokeys', tags=["Crypto Keys"])
    async def run_wrapper(req: Request) -> JSONResponse:
        return await cryptokeys_get_controller.run(req)


ca_container.wire(modules=[sys.modules[__name__]])
