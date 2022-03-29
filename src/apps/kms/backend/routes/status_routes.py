import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request

from src.apps.kms.backend.controllers.health.StatusGetController import StatusGetController
from src.apps.kms.backend.dependencies.KmsContainer import KmsContainer, kms_container


@inject
def register(
        router: APIRouter,
        status_get_controller: StatusGetController = Provide[KmsContainer.status_get_controller]
):
    @router.get('/status', tags=["Health"])
    async def run_wrapper(req: Request):
        return await status_get_controller.run(req)


kms_container.wire(modules=[sys.modules[__name__]])
