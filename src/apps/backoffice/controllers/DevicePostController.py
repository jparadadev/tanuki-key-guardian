from typing import Dict, Any

from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.backoffice.controllers.BackofficeController import BackofficeController
from src.contexts.backoffice.devices.application.create_one.CreateDeviceCommand import CreateDeviceCommand
from src.contexts.backoffice.devices.infrastructure.DevicesHttpResponseErrorHandler import JsonResponseErrorHandler
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.errors.DomainError import DomainError


class DevicePostController(BackofficeController):

    def __init__(
            self,
            command_bus: CommandBus,
    ):
        self._command_bus = command_bus
        self._error_handler = JsonResponseErrorHandler()

    async def run(self, req: Request) -> JSONResponse:
        body: Dict[str, Any] = await req.json()
        command: CreateDeviceCommand = CreateDeviceCommand(body['id'], body['name'])
        try:
            await self._command_bus.dispatch(command)
        except DomainError as err:
            return self._error_handler.resolve(err)

        return JSONResponse(status_code=HTTPStatus.CREATED)
