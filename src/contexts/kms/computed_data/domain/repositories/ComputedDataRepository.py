from src.contexts.kms.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.kms.computed_data.domain.entities.ComputedData import ComputedData
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.kms.computed_data.domain.entities.ComputedDataType import ComputedDataType
from src.contexts.shared.domain.Interface import Interface


class ComputedDataRepository(Interface):

    async def find_one_by_crypto_key_and_input(self, key: CryptoKey, input: ComputedDataInput,
                                               type: ComputedDataType) -> ComputedData:
        raise NotImplementedError()
