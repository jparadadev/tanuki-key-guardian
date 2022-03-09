import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.backoffice.backend.controllers.ClientsGetController import ClientsGetController
from src.apps.backoffice.backend.controllers.ClientPostController import ClientPostController
from src.apps.backoffice.backend.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container
from src.contexts.backoffice.clients.infrastructure.create_one.CreateClientCommandDto import CreateClientCommandDto


@inject
def register(
        router: APIRouter,
        clients_get_controller: ClientsGetController = Provide[BackofficeContainer.clients_get_controller],
        client_post_controller: ClientPostController = Provide[BackofficeContainer.client_post_controller],
):
    @router.post('/clients', tags=["Clients"])
    async def run_wrapper(_: CreateClientCommandDto, req: Request) -> JSONResponse:
        return await client_post_controller.run(req)

    @router.get('/clients', tags=["Clients"])
    async def run_wrapper(req: Request) -> JSONResponse:
        return await clients_get_controller.run(req)


backoffice_container.wire(modules=[sys.modules[__name__]])
