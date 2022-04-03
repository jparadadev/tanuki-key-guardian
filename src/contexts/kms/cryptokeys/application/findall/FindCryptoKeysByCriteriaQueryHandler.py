from src.contexts.kms.cryptokeys.application.findall.BackofficeCryptoKeysResponse import \
    BackofficeCryptoKeysResponse
from src.contexts.kms.cryptokeys.application.findall.CryptoKeysByCriteriaFinder import CryptoKeysByCriteriaFinder
from src.contexts.kms.cryptokeys.application.findall.FindCryptoKeysByCriteriaQuery import \
    FindCryptoKeysByCriteriaQuery
from src.contexts.shared.domain.QueryHandler import QueryHandler
from src.contexts.shared.domain.criteria.Criteria import Criteria


class FindCryptoKeysByCriteriaQueryHandler(QueryHandler):
    _subscription: str = FindCryptoKeysByCriteriaQuery.QUERY_TYPE

    def __init__(self, finder: CryptoKeysByCriteriaFinder):
        self._finder = finder

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, query: FindCryptoKeysByCriteriaQuery) -> BackofficeCryptoKeysResponse:
        criteria = Criteria(query.filters, query.order_by, query.limit)
        return await self._finder.run(criteria)
