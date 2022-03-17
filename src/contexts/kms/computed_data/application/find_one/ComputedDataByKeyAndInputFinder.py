from src.contexts.backoffice.cryptokeys.application.findall.BackofficeCryptoKeysResponse import \
    BackofficeCryptoKeysResponse
from src.contexts.backoffice.cryptokeys.domain.repositories.CryptoKeyRepository import CryptoKeyRepository
from src.contexts.kms.computed_data.application.find_one.KmsComputedDataResponse import KmsComputedDataResponse
from src.contexts.shared.domain.criteria.Criteria import Criteria


class ComputedDataByKeyAndInputFinder:

    def __init__(self, cryptokey_repository: CryptoKeyRepository):
        self._cryptokey_repository = cryptokey_repository

    async def run(self, criteria: Criteria) -> KmsComputedDataResponse:
        cryptokeys, criteria_metadata = await self._cryptokey_repository.find_by_criteria(criteria)
        return KmsComputedDataResponse(cryptokeys, criteria_metadata)

