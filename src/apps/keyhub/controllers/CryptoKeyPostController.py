from typing import Dict, Any

from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.keyhub.controllers.KeyhubController import KeyhubController
from src.contexts.backoffice.cryptokeys.application.create_one.CreateCryptoKeyCommand import CreateCryptoKeyCommand
from src.contexts.backoffice.cryptokeys.infrastructure.CryptoKeysHttpResponseErrorHandler import \
    JsonResponseErrorHandler
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.errors.DomainError import DomainError


class CryptoKeyPostController(KeyhubController):

    def __init__(
            self,
            command_bus: CommandBus,
    ):
        self._command_bus = command_bus
        self._error_handler = JsonResponseErrorHandler()

    async def run(self, req: Request) -> JSONResponse:
        body: Dict[str, Any] = await req.json()
        command: CreateCryptoKeyCommand = CreateCryptoKeyCommand(body.get('id'), body.get('client-id'),
                                                                 body.get('type'), body.get('payload'),
                                                                 body.get('is-master'))
        try:
            await self._command_bus.dispatch(command)
        except DomainError as err:
            return self._error_handler.resolve(err)

        return JSONResponse(status_code=HTTPStatus.CREATED)
