from typing import List, Tuple, Optional

from pymongo import MongoClient, ASCENDING

from src.contexts.ca.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.ca.cryptokeys.domain.repositories.CryptoKeyRepository import CryptoKeyRepository
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoRepository import PyMongoRepository
from src.contexts.shared.Infrastructure.persistence.mongo.parse_criteria_to_mongo_query import \
    parse_criteria_to_mongo_query
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class PyMongoCryptoKeyRepository(PyMongoRepository, CryptoKeyRepository):
    _COLLECTION_NAME = 'cryptokey'
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

    async def find_by_criteria_and_is_not_private(self, criteria: Criteria) -> Tuple[List[CryptoKey],
                                                                                     Optional[CriteriaQueryMetadata]]:
        raw_query, options = parse_criteria_to_mongo_query(criteria)
        raw_query['is-private'] = False
        results, count = await super()._find_by_raw_criteria(raw_query, options)
        entities = [CryptoKey.create_from_primitives(result) for result in results]
        metadata = CriteriaQueryMetadata(count)
        return entities, metadata
