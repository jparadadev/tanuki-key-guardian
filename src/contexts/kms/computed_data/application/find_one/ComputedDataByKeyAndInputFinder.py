from src.contexts.kms.computed_data.application.find_one.KmsComputedDataResponse import KmsComputedDataResponse
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.kms.computed_data.domain.entities.ComputedDataMeta import ComputedDataMeta
from src.contexts.kms.computed_data.domain.entities.ComputedDataType import ComputedDataType
from src.contexts.kms.computed_data.domain.repositories.ComputedDataRepository import ComputedDataRepository
from src.contexts.kms.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.kms.cryptokeys.domain.repositories.CryptoKeyRepository import CryptoKeyRepository


class ComputedDataByKeyAndInputFinder:

    def __init__(
            self,
            cryptokey_repository: CryptoKeyRepository,
            computed_data_repository: ComputedDataRepository,
    ):
        self._cryptokey_repository = cryptokey_repository
        self._computed_data_repository = computed_data_repository

    async def run(
            self,
            key_id: CryptoKeyId,
            cd_input: ComputedDataInput,
            cd_type: ComputedDataType,
            meta: ComputedDataMeta,
    ) -> KmsComputedDataResponse:
        crypto_key = await self._cryptokey_repository.find_by_id(key_id)
        res = await self._computed_data_repository.find_one_by_crypto_key_and_input(crypto_key, cd_input, cd_type, meta)
        return KmsComputedDataResponse(res)
