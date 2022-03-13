from typing import NoReturn

from src.contexts.backoffice.clients.domain.entities.ClientId import ClientId
from src.contexts.backoffice.cryptokeys.application.create_one.CreateCryptoKeyCommand import CreateCryptoKeyCommand
from src.contexts.backoffice.cryptokeys.application.create_one.CryptoKeyCreator import CryptoKeyCreator
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyPayload import CryptoKeyPayload
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyType
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.CommandHandler import CommandHandler


class CreateCryptoKeyCommandHandler(BaseObject, CommandHandler):

    _subscription: str = CreateCryptoKeyCommand.COMMAND_TYPE

    def __init__(self, creator: CryptoKeyCreator):
        self._creator = creator

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, command: CreateCryptoKeyCommand) -> NoReturn:
        cryptokey_id: CryptoKeyId = CryptoKeyId(command.id)
        client_id: ClientId = ClientId(command.id)
        cryptokey_type: CryptoKeyType = CryptoKeyType(command.cryptokey_type)
        payload: CryptoKeyPayload = CryptoKeyPayload(command.payload)
        await self._creator.run(cryptokey_id, client_id, cryptokey_type, payload)


