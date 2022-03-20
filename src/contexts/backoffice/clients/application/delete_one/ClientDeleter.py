from src.contexts.backoffice.clients.domain.entities.Client import Client
from src.contexts.backoffice.clients.domain.entities.ClientId import ClientId
from src.contexts.backoffice.clients.domain.entities.ClientName import ClientName
from src.contexts.backoffice.clients.domain.repositories.ClientRepository import ClientRepository
from src.contexts.shared.domain.EventBus import EventBus


class ClientDeleter:

    def __init__(self, client_repository: ClientRepository, event_bus: EventBus):
        self._client_repository = client_repository
        self._event_bus = event_bus

    async def run(self, client_id: ClientId):
        await self._client_repository.delete_one(client_id)
        # await self._event_bus.publish(client.pull_domain_events())
