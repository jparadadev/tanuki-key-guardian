from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class CreateDeviceCommand(BaseObject, Command):

    COMMAND_TYPE: str = 'backoffice.create-one.device'

    def __init__(self, device_id: str, name: str):
        self.id = device_id
        self.name = name

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
