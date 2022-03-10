from datetime import datetime
from typing import Dict, List, Union, Any

from src.contexts.backoffice.clients.domain.create_one.ClientCreatedDomainEvent import ClientCreatedDomainEvent
from src.contexts.backoffice.clients.domain.entities.ClientCreationDate import ClientCreationDate
from src.contexts.backoffice.clients.domain.entities.ClientId import ClientId
from src.contexts.backoffice.clients.domain.entities.ClientName import ClientName
from src.contexts.backoffice.cryptokeys.domain.create_one.CryptoKeyCreatedDomainEvent import CryptoKeyCreatedDomainEvent
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyCreationDate import CryptoKeyCreationDate
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyType
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class CryptoKey(AggregateRoot):

    def __init__(self, cryptokey_id: CryptoKeyId, client_id: ClientId, cryptokey_type: CryptoKeyType, created_at: CryptoKeyCreationDate):
        super().__init__()
        self.id = cryptokey_id
        self.client_id = client_id
        self.type = cryptokey_type
        self.created_at = created_at

    @staticmethod
    def create(cryptokey_id: CryptoKeyId, client_id: ClientId, cryptokey_type: CryptoKeyType):
        now = CryptoKeyCreationDate(datetime.now())
        cryptokey = CryptoKey(cryptokey_id, client_id, cryptokey_type, now)
        event = CryptoKeyCreatedDomainEvent(cryptokey.id.value(), cryptokey)
        cryptokey.record_event(event)
        return cryptokey

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        client = CryptoKey(
            CryptoKeyId(raw_data.get('id')),
            ClientId(raw_data.get('client-id')),
            CryptoKeyType(raw_data.get('name')),
            CryptoKeyCreationDate(raw_data.get('created-at')),
        )
        return client

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'type': self.type.value(),
            'client-id': self.client_id.value(),
            'created-at': self.created_at.value(),
        }
