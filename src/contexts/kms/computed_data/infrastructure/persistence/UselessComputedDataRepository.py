from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.kms.computed_data.domain.entities.ComputedData import ComputedData
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.kms.computed_data.domain.entities.ComputedDataOutput import ComputedDataOutput
from src.contexts.kms.computed_data.domain.repositories.ComputedDataRepository import ComputedDataRepository
from src.contexts.shared.domain.BaseObject import BaseObject


class UselessComputedDataRepository(BaseObject, ComputedDataRepository):

    async def find_one_by_crypto_key_and_input(self, key: CryptoKey, input: ComputedDataInput) -> ComputedData:
        data = ComputedData(
            input,
            ComputedDataOutput(input.value()),
            key.id,
        )
        return data