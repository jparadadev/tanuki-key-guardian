from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class CreateCryptoKeyCommand(BaseObject, Command):

    COMMAND_TYPE: str = 'backoffice.cryptokey.create-one'

    def __init__(self, cryptokey_id: str, client_id: str, cryptokey_type: str):
        self.id = cryptokey_id
        self.client_id = client_id
        self.cryptokey_type = cryptokey_type

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
