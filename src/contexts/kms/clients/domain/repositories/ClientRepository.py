from abc import ABC
from typing import List, NoReturn, Tuple, Optional

from src.contexts.kms.clients.domain.entities.Client import Client
from src.contexts.kms.clients.domain.entities.ClientId import ClientId
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class ClientRepository(ABC):

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[Client], Optional[CriteriaQueryMetadata]]:
        raise NotImplementedError()

    async def create_one(self, client: Client) -> NoReturn:
        raise NotImplementedError()

    async def delete_one(self, client_id: ClientId) -> NoReturn:
        raise NotImplementedError()
