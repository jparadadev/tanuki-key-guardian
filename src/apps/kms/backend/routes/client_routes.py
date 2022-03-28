import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.kms.backend.controllers.ClientDeleteController import ClientDeleteController
from src.apps.kms.backend.controllers.ClientsGetController import ClientsGetController
from src.apps.kms.backend.controllers.ClientPostController import ClientPostController
from src.apps.kms.backend.dependencies.KmsContainer import KmsContainer, kms_container
from src.apps.kms.backend.dtos.CreateClientCommandDto import CreateClientCommandDto


@inject
def register(
        router: APIRouter,
        clients_get_controller: ClientsGetController = Provide[KmsContainer.clients_get_controller],
        client_post_controller: ClientPostController = Provide[KmsContainer.client_post_controller],
        client_delete_controller: ClientDeleteController = Provide[KmsContainer.client_post_controller],
):
    @router.post('/clients', tags=["Clients"])
    async def run_wrapper(_: CreateClientCommandDto, req: Request) -> JSONResponse:
        return await client_post_controller.run(req)

    @router.get('/clients', tags=["Clients"])
    async def run_wrapper(req: Request) -> JSONResponse:
        return await clients_get_controller.run(req)

    @router.delete('/clients/{client_id}', tags=["Clients"])
    async def run_wrapper(client_id: str, req: Request) -> JSONResponse:
        return await client_delete_controller.run(req)


kms_container.wire(modules=[sys.modules[__name__]])
