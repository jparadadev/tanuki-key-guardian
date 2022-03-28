from typing import NoReturn

from src.contexts.kms.clients.application.create_one.CreateClientCommand import CreateClientCommand
from src.contexts.kms.clients.application.create_one.ClientCreator import ClientCreator
from src.contexts.kms.clients.domain.entities.ClientId import ClientId
from src.contexts.kms.clients.domain.entities.ClientName import ClientName
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.CommandHandler import CommandHandler


class CreateClientCommandHandler(BaseObject, CommandHandler):

    _subscription: str = CreateClientCommand.COMMAND_TYPE

    def __init__(self, creator: ClientCreator):
        self._creator = creator

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, command: CreateClientCommand) -> NoReturn:
        client_id: ClientId = ClientId(command.id)
        client_name: ClientName = ClientName(command.name)
        await self._creator.run(client_id, client_name)


