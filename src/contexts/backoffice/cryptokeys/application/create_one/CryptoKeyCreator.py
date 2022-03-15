from src.contexts.backoffice.clients.domain.entities.ClientId import ClientId
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyIsMaster import CryptoKeyIsMaster
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyIsPrivate import CryptoKeyIsPrivate
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyPayload import CryptoKeyPayload
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyType
from src.contexts.backoffice.cryptokeys.domain.repositories.CryptoKeyRepository import CryptoKeyRepository
from src.contexts.shared.domain.EventBus import EventBus


class CryptoKeyCreator:

    def __init__(self, cryptokey_repository: CryptoKeyRepository, event_bus: EventBus):
        self._cryptokey_repository = cryptokey_repository
        self._event_bus = event_bus

    async def run(self, cryptokey_id: CryptoKeyId, client_id: ClientId, cryptokey_type: CryptoKeyType,
                  payload: CryptoKeyPayload, is_master: CryptoKeyIsMaster, is_private: CryptoKeyIsPrivate):
        cryptokey: CryptoKey = CryptoKey.create(cryptokey_id, client_id, cryptokey_type, payload, is_master, is_private)
        await self._cryptokey_repository.create_one(cryptokey)
        await self._event_bus.publish(cryptokey.pull_domain_events())
