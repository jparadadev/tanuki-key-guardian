import random

from src.contexts.kms.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.kms.cryptokeys.domain.entities.CryptoKeyPayload import CryptoKeyPayload
from src.contexts.kms.cryptokeys.domain.repositories.CryptoKeyRepository import CryptoKeyRepository
from src.contexts.shared.domain.EventBus import EventBus


class CryptoKeyRotator:

    def __init__(self, cryptokey_repository: CryptoKeyRepository, event_bus: EventBus):
        self._cryptokey_repository = cryptokey_repository
        self._event_bus = event_bus

    async def run(self, key_id: CryptoKeyId):
        crypto_key = await self._cryptokey_repository.find_by_id(key_id)
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        length = 62

        def uid(seed):
            random.seed(seed)
            return ''.join([chars[int(random.random() * length)] for _ in range(len(crypto_key.payload.value()))])

        # TODO: rotation
        uid(crypto_key.payload.value())
        rote = uid(crypto_key.payload.value())
        crypto_key.payload = CryptoKeyPayload(rote)
        await self._cryptokey_repository.update_one(crypto_key)
        # TODO: dispatch key rotated event
