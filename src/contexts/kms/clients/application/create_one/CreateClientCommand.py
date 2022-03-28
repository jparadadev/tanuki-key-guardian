from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class CreateClientCommand(BaseObject, Command):

    COMMAND_TYPE: str = 'kms.create-one.clients'

    def __init__(self, client_id: str, name: str):
        self.id = client_id
        self.name = name

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
