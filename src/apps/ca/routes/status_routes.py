import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request

from src.apps.ca.controllers.StatusGetController import StatusGetController
from src.apps.ca.dependencies.CaContainer import CaContainer, ca_container


@inject
def register(
        router: APIRouter,
        status_get_controller: StatusGetController = Provide[CaContainer.status_get_controller]
):
    @router.get('/status', tags=["Health"])
    async def run_wrapper(req: Request):
        return await status_get_controller.run(req)


ca_container.wire(modules=[sys.modules[__name__]])
