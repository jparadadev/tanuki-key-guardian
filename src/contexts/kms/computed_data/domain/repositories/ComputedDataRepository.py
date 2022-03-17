from src.contexts.kms.computed_data.domain.entities.ComputedData import ComputedData
from src.contexts.shared.domain.Interface import Interface


class ComputedDataRepository(Interface):

    async def find_one_by_crypto_key_and_input(self) -> ComputedData:
        raise NotImplementedError()
