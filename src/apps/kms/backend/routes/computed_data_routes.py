import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Query
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
    async def run_wrapper(req: Request, input=Query(None), key_id=Query(None, alias='key-id'),
                          type=Query(None)) -> JSONResponse:
        return await computed_data_get_controller.run(req)


kms_container.wire(modules=[sys.modules[__name__]])
