from src.contexts.kms.cryptokeys.application.find_all_not_private.BackofficeCryptoKeysResponse import \
    BackofficeCryptoKeysResponse
from src.contexts.ca.cryptokeys.domain.repositories.CryptoKeyRepository import CryptoKeyRepository
from src.contexts.shared.domain.criteria.Criteria import Criteria


class CryptoKeysByCriteriaAndNotPrivateFinder:

    def __init__(self, cryptokey_repository: CryptoKeyRepository):
        self._cryptokey_repository = cryptokey_repository

    async def run(self, criteria: Criteria) -> BackofficeCryptoKeysResponse:
        cryptokeys, criteria_metadata = await self._cryptokey_repository.find_by_criteria_and_is_not_private(criteria)
        return BackofficeCryptoKeysResponse(cryptokeys, criteria_metadata)

