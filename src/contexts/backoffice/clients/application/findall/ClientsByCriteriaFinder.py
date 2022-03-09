from src.contexts.backoffice.clients.application.findall.BackofficeClientsResponse import BackofficeClientsResponse
from src.contexts.backoffice.clients.domain.repositories.ClientRepository import ClientRepository
from src.contexts.shared.domain.criteria.Criteria import Criteria


class ClientsByCriteriaFinder:

    def __init__(self, client_repository: ClientRepository):
        self._client_repository = client_repository

    async def run(self, criteria: Criteria) -> BackofficeClientsResponse:
        clients, criteria_metadata = await self._client_repository.find_by_criteria(criteria)
        return BackofficeClientsResponse(clients, criteria_metadata)

