import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Header
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.kms.backend.controllers.computed_data.ComputedDataGetController import ComputedDataGetController
from src.apps.kms.backend.dependencies.KmsContainer import kms_container, KmsContainer


@inject
def register(
        router: APIRouter,
        computed_data_get_controller: ComputedDataGetController = Provide[KmsContainer.computed_data_get_controller],
):
    @router.get('/computed', tags=["Computed Data"])
    async def run_wrapper(req: Request, input=Header(None, alias='X-Input'), key_id=Header(None, alias='X-Key-Id'),
                          type=Header(None, alias='X-Type'), iv=Header(None, alias='X-Iv'),
                          nonce=Header(None, alias='X-Nonce')) -> JSONResponse:
        return await computed_data_get_controller.run(req)


kms_container.wire(modules=[sys.modules[__name__]])
