from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class DeleteClientCommand(BaseObject, Command):
    COMMAND_TYPE: str = 'kms.delete-one.clients'

    def __init__(self, client_id: str):
        self.id = client_id

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
