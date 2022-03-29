from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.kms.backend.controllers.KmsController import KmsController
from src.contexts.kms.cryptokeys.application.rotate_one.RotateCryptoKeyCommand import RotateCryptoKeyCommand
from src.contexts.kms.cryptokeys.infrastructure.CryptoKeysHttpResponseErrorHandler import \
    JsonResponseErrorHandler
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.errors.DomainError import DomainError


class RotateCryptoKeyPutController(KmsController):

    def __init__(
            self,
            command_bus: CommandBus,
    ):
        self._command_bus = command_bus
        self._error_handler = JsonResponseErrorHandler()

    async def run(self, req: Request) -> JSONResponse:
        params = req.path_params
        command = RotateCryptoKeyCommand(params.get('key-id'))
        try:
            await self._command_bus.dispatch(command)
        except DomainError as err:
            return self._error_handler.resolve(err)

        return JSONResponse(status_code=HTTPStatus.CREATED)
