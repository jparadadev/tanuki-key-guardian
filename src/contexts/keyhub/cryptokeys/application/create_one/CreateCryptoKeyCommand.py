from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class CreateCryptoKeyCommand(BaseObject, Command):

    COMMAND_TYPE: str = 'keyhub.cryptokey.create-one'

    def __init__(self, cryptokey_id: str, client_id: str, cryptokey_type: str, payload: str, is_master: bool):
        self.id = cryptokey_id
        self.client_id = client_id
        self.cryptokey_type = cryptokey_type
        self.payload = payload
        self.is_master = is_master

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
