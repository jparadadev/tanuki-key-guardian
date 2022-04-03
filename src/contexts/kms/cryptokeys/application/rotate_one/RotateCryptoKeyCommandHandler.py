from typing import NoReturn

from src.contexts.kms.cryptokeys.application.rotate_one.CryptoKeyRotator import CryptoKeyRotator
from src.contexts.kms.cryptokeys.application.rotate_one.RotateCryptoKeyCommand import RotateCryptoKeyCommand
from src.contexts.kms.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.CommandHandler import CommandHandler


class RotateCryptoKeyCommandHandler(BaseObject, CommandHandler):
    _subscription: str = RotateCryptoKeyCommand.COMMAND_TYPE

    def __init__(self, rotator: CryptoKeyRotator):
        self._rotator = rotator

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, command: RotateCryptoKeyCommand) -> NoReturn:
        cryptokey_id: CryptoKeyId = CryptoKeyId(command.id)
        await self._rotator.run(cryptokey_id)
