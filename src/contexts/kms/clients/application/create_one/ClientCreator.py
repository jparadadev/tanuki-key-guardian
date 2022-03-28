from src.contexts.kms.clients.domain.entities.Client import Client
from src.contexts.kms.clients.domain.entities.ClientId import ClientId
from src.contexts.kms.clients.domain.entities.ClientName import ClientName
from src.contexts.kms.clients.domain.repositories.ClientRepository import ClientRepository
from src.contexts.shared.domain.EventBus import EventBus


class ClientCreator:

    def __init__(self, client_repository: ClientRepository, event_bus: EventBus):
        self._client_repository = client_repository
        self._event_bus = event_bus

    async def run(self, client_id: ClientId, client_name: ClientName):
        client: Client = Client.create(client_id, client_name)
        await self._client_repository.create_one(client)
        await self._event_bus.publish(client.pull_domain_events())
