from src.contexts.backoffice.cryptokeys.application.findall.BackofficeCryptoKeysResponse import \
    BackofficeCryptoKeysResponse
from src.contexts.backoffice.cryptokeys.domain.repositories.CryptoKeyRepository import CryptoKeyRepository
from src.contexts.shared.domain.criteria.Criteria import Criteria


class CryptoKeysByCriteriaFinder:

    def __init__(self, cryptokey_repository: CryptoKeyRepository):
        self._cryptokey_repository = cryptokey_repository

    async def run(self, criteria: Criteria) -> BackofficeCryptoKeysResponse:
        cryptokeys, criteria_metadata = await self._cryptokey_repository.find_by_criteria(criteria)
        return BackofficeCryptoKeysResponse(cryptokeys, criteria_metadata)

