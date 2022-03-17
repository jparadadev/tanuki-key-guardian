from src.contexts.backoffice.cryptokeys.application.findall.BackofficeCryptoKeysResponse import \
    BackofficeCryptoKeysResponse
from src.contexts.kms.computed_data.application.find_one.ComputedDataByKeyAndInputFinder import \
    ComputedDataByKeyAndInputFinder
from src.contexts.kms.computed_data.application.find_one.ComputedDataByKeyAndInputQuery import \
    ComputedDataByKeyAndInputQuery
from src.contexts.shared.domain.QueryHandler import QueryHandler
from src.contexts.shared.domain.criteria.Criteria import Criteria


class ComputedDataByKeyAndInputQueryHandler(QueryHandler):

    _subscription: str = ComputedDataByKeyAndInputQuery.QUERY_TYPE

    def __init__(self, finder: ComputedDataByKeyAndInputFinder):
        self._finder = finder

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, query: ComputedDataByKeyAndInputQuery) -> BackofficeCryptoKeysResponse:
        criteria = Criteria(query.filters, query.order_by, query.limit)
        return await self._finder.run(criteria)
