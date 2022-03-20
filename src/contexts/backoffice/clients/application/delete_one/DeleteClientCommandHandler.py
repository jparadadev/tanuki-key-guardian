from typing import NoReturn

from src.contexts.backoffice.clients.application.create_one.CreateClientCommand import CreateClientCommand
from src.contexts.backoffice.clients.application.create_one.ClientCreator import ClientCreator
from src.contexts.backoffice.clients.application.delete_one.ClientDeleter import ClientDeleter
from src.contexts.backoffice.clients.domain.entities.ClientId import ClientId
from src.contexts.backoffice.clients.domain.entities.ClientName import ClientName
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.CommandHandler import CommandHandler


class DeleteClientCommandHandler(BaseObject, CommandHandler):

    _subscription: str = CreateClientCommand.COMMAND_TYPE

    def __init__(self, deleter: ClientDeleter):
        self._deleter = deleter

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, command: CreateClientCommand) -> NoReturn:
        client_id: ClientId = ClientId(command.id)
        await self._deleter.run(client_id)


