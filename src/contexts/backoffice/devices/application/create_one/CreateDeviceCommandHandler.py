from typing import NoReturn

from src.contexts.backoffice.devices.application.create_one.CreateDeviceCommand import CreateDeviceCommand
from src.contexts.backoffice.devices.application.create_one.DeviceCreator import DeviceCreator
from src.contexts.backoffice.devices.domain.entities.DeviceId import DeviceId
from src.contexts.backoffice.devices.domain.entities.DeviceName import DeviceName
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.CommandHandler import CommandHandler


class CreateDeviceCommandHandler(BaseObject, CommandHandler):

    _subscription: str = CreateDeviceCommand.COMMAND_TYPE

    def __init__(self, creator: DeviceCreator):
        self._creator = creator

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, command: CreateDeviceCommand) -> NoReturn:
        device_id: DeviceId = DeviceId(command.id)
        device_name: DeviceName = DeviceName(command.name)
        await self._creator.run(device_id, device_name)


