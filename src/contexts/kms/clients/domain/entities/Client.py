from datetime import datetime
from typing import Dict, List, Union, Any

from src.contexts.kms.clients.domain.create_one.ClientCreatedDomainEvent import ClientCreatedDomainEvent
from src.contexts.kms.clients.domain.entities.ClientCreationDate import ClientCreationDate
from src.contexts.kms.clients.domain.entities.ClientId import ClientId
from src.contexts.kms.clients.domain.entities.ClientName import ClientName
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class Client(AggregateRoot):

    def __init__(self, client_id: ClientId, name: ClientName, created_at: ClientCreationDate):
        super().__init__()
        self.id = client_id
        self.name = name
        self.created_at = created_at

    @staticmethod
    def create(client_id: ClientId, name: ClientName):
        now = ClientCreationDate(datetime.now())
        client = Client(client_id, name, now)
        event = ClientCreatedDomainEvent(client.id.value(), client)
        client.record_event(event)
        return client

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        client = Client(
            ClientId(raw_data.get('id')),
            ClientName(raw_data.get('name')),
            ClientCreationDate(raw_data.get('created-at')),
        )
        return client

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'name': self.name.value(),
            'created-at': self.created_at.value(),
        }
