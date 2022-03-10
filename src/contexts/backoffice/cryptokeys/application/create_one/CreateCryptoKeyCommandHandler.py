from typing import NoReturn

from src.contexts.backoffice.clients.application.create_one.CreateClientCommand import CreateClientCommand
from src.contexts.backoffice.clients.application.create_one.ClientCreator import ClientCreator
from src.contexts.backoffice.clients.domain.entities.ClientId import ClientId
from src.contexts.backoffice.clients.domain.entities.ClientName import ClientName
from src.contexts.backoffice.cryptokeys.application.create_one.CreateCryptoKeyCommand import CreateCryptoKeyCommand
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyType
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.CommandHandler import CommandHandler


class CreateCryptoKeyCommandHandler(BaseObject, CommandHandler):

    _subscription: str = CreateClientCommand.COMMAND_TYPE

    def __init__(self, creator: ClientCreator):
        self._creator = creator

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, command: CreateCryptoKeyCommand) -> NoReturn:
        cryptokey_id: CryptoKeyId = CryptoKeyId(command.id)
        client_id: ClientId = ClientId(command.id)
        cryptokey_type: CryptoKeyType = CryptoKeyType(command.cryptokey_type)
        await self._creator.run(cryptokey_id, client_id, cryptokey_type)


