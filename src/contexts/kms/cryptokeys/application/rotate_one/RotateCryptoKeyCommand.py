from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class RotateCryptoKeyCommand(BaseObject, Command):

    COMMAND_TYPE: str = 'kms.cryptokey.rotate'

    def __init__(self, cryptokey_id: str):
        self.id = cryptokey_id

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
