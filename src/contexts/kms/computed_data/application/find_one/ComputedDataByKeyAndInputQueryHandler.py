from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.kms.computed_data.application.find_one.ComputedDataByKeyAndInputFinder import \
    ComputedDataByKeyAndInputFinder
from src.contexts.kms.computed_data.application.find_one.ComputedDataByKeyAndInputQuery import \
    ComputedDataByKeyAndInputQuery
from src.contexts.kms.computed_data.application.find_one.KmsComputedDataResponse import KmsComputedDataResponse
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.kms.computed_data.domain.entities.ComputedDataType import ComputedDataType
from src.contexts.shared.domain.QueryHandler import QueryHandler


class ComputedDataByKeyAndInputQueryHandler(QueryHandler):

    _subscription: str = ComputedDataByKeyAndInputQuery.QUERY_TYPE

    def __init__(self, finder: ComputedDataByKeyAndInputFinder):
        self._finder = finder

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, query: ComputedDataByKeyAndInputQuery) -> KmsComputedDataResponse:
        crypto_key_id = CryptoKeyId(query.key_id)
        input = ComputedDataInput(query.input)
        cd_type = ComputedDataType(query.type)
        return await self._finder.run(crypto_key_id, input, cd_type)
