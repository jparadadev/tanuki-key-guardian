from src.contexts.backoffice.device.application.findall.BackofficeDevicesResponse import BackofficeDevicesResponse
from src.contexts.backoffice.device.application.findall.DevicesByCriteriaFinder import DevicesByCriteriaFinder
from src.contexts.backoffice.device.application.findall.FindDevicesByCriteriaQuery import FindDevicesByCriteriaQuery
from src.contexts.shared.domain.QueryHandler import QueryHandler
from src.contexts.shared.domain.criteria.Criteria import Criteria


class FindDevicesByCriteriaQueryHandler(QueryHandler):

    _subscription: str = FindDevicesByCriteriaQuery.QUERY_TYPE

    def __init__(self, finder: DevicesByCriteriaFinder):
        self._finder = finder

    def subscribed_to(self) -> str:
        return self._subscription

    async def handle(self, query: FindDevicesByCriteriaQuery) -> BackofficeDevicesResponse:
        criteria = Criteria(query.filters, query.order_by, query.limit)
        return await self._finder.run(criteria)
