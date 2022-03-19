import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Query
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.backoffice.backend.controllers.CryptoKeyPostController import CryptoKeyPostController
from src.apps.backoffice.backend.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container
from src.apps.kms.controllers.ComputedDataGetController import ComputedDataGetController
from src.apps.kms.dependencies import KmsContainer
from src.apps.kms.dependencies.KmsContainer import computed_data_container, KeyhubContainer
from src.contexts.backoffice.cryptokeys.infrastructure.create_one.CreateCryptoKeyCommandDto import \
    CreateCryptoKeyCommandDto


@inject
def register(
        router: APIRouter,
        computed_data_get_controller: ComputedDataGetController = Provide[KeyhubContainer.computed_data_get_controller],
):
    @router.get('/computed', tags=["Computed Data"])
    async def run_wrapper(req: Request, input=Query(None), key_id=Query(None, alias='key-id')) -> JSONResponse:
        return await computed_data_get_controller.run(req)


computed_data_container.wire(modules=[sys.modules[__name__]])
