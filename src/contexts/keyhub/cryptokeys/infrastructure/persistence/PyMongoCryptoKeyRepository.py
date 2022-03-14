from typing import List, NoReturn, Tuple, Optional

from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError

from src.contexts.keyhub.cryptokeys.domain.create_one.CryptoAlreadyExistsError import CryptoKeyAlreadyExistsError
from src.contexts.keyhub.cryptokeys.domain.entities.ClientId import ClientId
from src.contexts.keyhub.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.keyhub.cryptokeys.domain.entities.CryptoKeyIsMaster import CryptoKeyIsMaster
from src.contexts.keyhub.cryptokeys.domain.repositories.CryptoKeyRepository import CryptoKeyRepository
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoRepository import PyMongoRepository
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

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[CryptoKey], Optional[CriteriaQueryMetadata]]:
        results, count = await super()._find_by_criteria(criteria)
        entities = [CryptoKey.create_from_primitives(result) for result in results]
        metadata = CriteriaQueryMetadata(count)
        return entities, metadata

    async def create_one(self, cryptokey: CryptoKey) -> NoReturn:
        try:
            cryptokey = await super()._create_one(cryptokey.to_primitives())
            return cryptokey
        except DuplicateKeyError as _:
            raise CryptoKeyAlreadyExistsError('CryptoKey with ID <{}> already exists.'.format(cryptokey.id.value()))

    async def find_by_client_and_is_master(self, client: ClientId, is_master: CryptoKeyIsMaster) -> \
            Tuple[Optional[CryptoKey], Optional[CriteriaQueryMetadata]]:
        pass
