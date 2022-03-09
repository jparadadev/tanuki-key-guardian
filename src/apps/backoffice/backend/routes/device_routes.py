import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.backoffice.backend.controllers.DevicesGetController import DevicesGetController
from src.apps.backoffice.backend.controllers.DevicePostController import DevicePostController
from src.apps.backoffice.backend.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container


@inject
def register(
        router: APIRouter,
        devices_get_controller: DevicesGetController = Provide[BackofficeContainer.devices_get_controller],
        device_post_controller: DevicePostController = Provide[BackofficeContainer.device_post_controller],
):
    @router.post('/devices', tags=["Devices"])
    async def run_wrapper(req: Request) -> JSONResponse:
        return await device_post_controller.run(req)

    @router.get('/devices', tags=["Devices"])
    async def run_wrapper(req: Request) -> JSONResponse:
        return await devices_get_controller.run(req)


backoffice_container.wire(modules=[sys.modules[__name__]])
