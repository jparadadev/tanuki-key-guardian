from src.contexts.kms.cryptokeys.application.find_all_not_private.BackofficeCryptoKeysResponse import \
    BackofficeCryptoKeysResponse
from src.contexts.kms.cryptokeys.application.find_all_not_private.CryptoKeysByCriteriaAndNotPrivateFinder import \
    CryptoKeysByCriteriaAndNotPrivateFinder
from src.contexts.kms.cryptokeys.application.find_all_not_private.FindCryptoKeysByCriteriaAndNotPrivateQuery import \
    FindCryptoKeysByCriteriaAndNotPrivateQuery
from src.contexts.shared.domain.QueryHandler import QueryHandler
from src.contexts.shared.domain.criteria.Criteria import Criteria


class FindCryptoKeysByCriteriaAndNotPrivateQueryHandler(QueryHandler):

    _subscription: str = FindCryptoKeysByCriteriaAndNotPrivateQuery.QUERY_TYPE

    def __init__(self, finder: CryptoKeysByCriteriaAndNotPrivateFinder):
        self._finder = finder

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, query: FindCryptoKeysByCriteriaAndNotPrivateQuery) -> BackofficeCryptoKeysResponse:
        criteria = Criteria(query.filters, query.order_by, query.limit)
        return await self._finder.run(criteria)
