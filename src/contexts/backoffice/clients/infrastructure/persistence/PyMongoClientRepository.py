from typing import List, NoReturn, Tuple, Optional

from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError

from src.contexts.backoffice.clients.domain.entities.Client import Client
from src.contexts.backoffice.clients.domain.create_one.ClientAlreadyExistsError import ClientAlreadyExistsError
from src.contexts.backoffice.clients.domain.repositories.ClientRepository import ClientRepository
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoRepository import PyMongoRepository
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class PyMongoClientRepository(PyMongoRepository, ClientRepository):

    _COLLECTION_NAME = 'clients'
    _DATABASE_NAME = 'tanuki-key-guardian'

    def __init__(self, client: MongoClient):
        super().__init__(client)
        super()._get_collection().create_index([
            ('id', ASCENDING)
        ], unique=True)

    def get_database_name(self):
        return self._DATABASE_NAME

    def get_collection_name(self):
        return self._COLLECTION_NAME

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[Client], Optional[CriteriaQueryMetadata]]:
        results, count = await super()._find_by_criteria(criteria)
        entities = [Client.create_from_primitives(result) for result in results]
        metadata = CriteriaQueryMetadata(count)
        return entities, metadata

    async def create_one(self, client: Client) -> NoReturn:
        try:
            client = await super()._create_one(client.to_primitives())
            return client
        except DuplicateKeyError as _:
            raise ClientAlreadyExistsError('Client with ID <{}> already exists.'.format(client.id.value()))
