from http import HTTPStatus

from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.kms.backend.controllers.KmsController import KmsController
from src.contexts.kms.clients.application.delete_one.DeleteClientCommand import DeleteClientCommand
from src.contexts.kms.clients.infrastructure.ClientsHttpResponseErrorHandler import JsonResponseErrorHandler
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.errors.DomainError import DomainError


class ClientDeleteController(KmsController):

    def __init__(
            self,
            command_bus: CommandBus,
    ):
        self._command_bus = command_bus
        self._error_handler = JsonResponseErrorHandler()

    async def run(self, req: Request) -> JSONResponse:
        params = dict(req.path_params)
        command = DeleteClientCommand(params.get('client_id'))
        try:
            await self._command_bus.dispatch(command)
        except DomainError as err:
            return self._error_handler.resolve(err)

        return JSONResponse(status_code=HTTPStatus.ACCEPTED)
