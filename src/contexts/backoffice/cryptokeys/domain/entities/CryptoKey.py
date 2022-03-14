from datetime import datetime
from typing import Dict, List, Union, Any

from src.contexts.backoffice.clients.domain.entities.ClientId import ClientId
from src.contexts.backoffice.cryptokeys.domain.create_one.CryptoKeyCreatedDomainEvent import CryptoKeyCreatedDomainEvent
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyCreationDate import CryptoKeyCreationDate
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyIsMaster import CryptoKeyIsMaster
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyPayload import CryptoKeyPayload
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyType
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class CryptoKey(AggregateRoot):

    def __init__(self, cryptokey_id: CryptoKeyId, client_id: ClientId, cryptokey_type: CryptoKeyType,
                 payload: CryptoKeyPayload, created_at: CryptoKeyCreationDate, is_master: CryptoKeyIsMaster):
        super().__init__()
        self.id = cryptokey_id
        self.client_id = client_id
        self.type = cryptokey_type
        self.payload = payload
        self.created_at = created_at
        self.is_master = is_master

    @staticmethod
    def create(cryptokey_id: CryptoKeyId, client_id: ClientId, cryptokey_type: CryptoKeyType,
               payload: CryptoKeyPayload, is_master: CryptoKeyIsMaster):
        now = CryptoKeyCreationDate(datetime.now())
        cryptokey = CryptoKey(cryptokey_id, client_id, cryptokey_type, payload, now, is_master)
        event = CryptoKeyCreatedDomainEvent(cryptokey.id.value(), cryptokey)
        cryptokey.record_event(event)
        return cryptokey

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        client = CryptoKey(
            CryptoKeyId(raw_data.get('id')),
            ClientId(raw_data.get('client-id')),
            CryptoKeyType(raw_data.get('type')),
            CryptoKeyPayload(raw_data.get('payload')),
            CryptoKeyCreationDate(raw_data.get('created-at')),
            CryptoKeyIsMaster(raw_data.get('is-master')),
        )
        return client

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'type': self.type.value(),
            'client-id': self.client_id.value(),
            'payload': self.payload.value(),
            'created-at': self.created_at.value(),
            'is-master': self.is_master.value(),
        }
