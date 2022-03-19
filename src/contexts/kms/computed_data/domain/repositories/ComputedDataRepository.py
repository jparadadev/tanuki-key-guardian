from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.kms.computed_data.domain.entities.ComputedData import ComputedData
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.shared.domain.Interface import Interface


class ComputedDataRepository(Interface):

    async def find_one_by_crypto_key_and_input(self, key: CryptoKey, input: ComputedDataInput) -> ComputedData:
        raise NotImplementedError()