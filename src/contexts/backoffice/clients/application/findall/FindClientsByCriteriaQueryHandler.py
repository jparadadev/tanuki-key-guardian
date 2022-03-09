from src.contexts.backoffice.clients.application.findall.BackofficeClientsResponse import BackofficeClientsResponse
from src.contexts.backoffice.clients.application.findall.ClientsByCriteriaFinder import ClientsByCriteriaFinder
from src.contexts.backoffice.clients.application.findall.FindClientsByCriteriaQuery import FindClientsByCriteriaQuery
from src.contexts.shared.domain.QueryHandler import QueryHandler
from src.contexts.shared.domain.criteria.Criteria import Criteria


class FindClientsByCriteriaQueryHandler(QueryHandler):

    _subscription: str = FindClientsByCriteriaQuery.QUERY_TYPE

    def __init__(self, finder: ClientsByCriteriaFinder):
        self._finder = finder

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, query: FindClientsByCriteriaQuery) -> BackofficeClientsResponse:
        criteria = Criteria(query.filters, query.order_by, query.limit)
        return await self._finder.run(criteria)
