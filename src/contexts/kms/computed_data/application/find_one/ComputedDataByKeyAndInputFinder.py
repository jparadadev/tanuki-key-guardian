from src.contexts.backoffice.cryptokeys.application.findall.BackofficeCryptoKeysResponse import \
    BackofficeCryptoKeysResponse
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.backoffice.cryptokeys.domain.repositories.CryptoKeyRepository import CryptoKeyRepository
from src.contexts.kms.computed_data.application.find_one.KmsComputedDataResponse import KmsComputedDataResponse
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.kms.computed_data.domain.entities.ComputedDataType import ComputedDataType
from src.contexts.kms.computed_data.domain.repositories.ComputedDataRepository import ComputedDataRepository
from src.contexts.shared.domain.criteria.Criteria import Criteria


class ComputedDataByKeyAndInputFinder:

    def __init__(
            self,
            cryptokey_repository: CryptoKeyRepository,
            computed_data_repository: ComputedDataRepository,
    ):
        self._cryptokey_repository = cryptokey_repository
        self._computed_data_repository = computed_data_repository

    async def run(self, key_id: CryptoKeyId, input: ComputedDataInput,
                  cd_type: ComputedDataType) -> KmsComputedDataResponse:
        crypto_key = await self._cryptokey_repository.find_by_id(key_id)
        res = await self._computed_data_repository.find_one_by_crypto_key_and_input(crypto_key, input, cd_type)
        return KmsComputedDataResponse(res)

