from abc import ABC
from typing import List, NoReturn, Tuple, Optional

from src.contexts.kms.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.kms.cryptokeys.domain.entities.ClientId import ClientId
from src.contexts.kms.cryptokeys.domain.entities.CryptoKeyIsMaster import CryptoKeyIsMaster
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class CryptoKeyRepository(ABC):

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[CryptoKey], Optional[CriteriaQueryMetadata]]:
        raise NotImplementedError()

    async def create_one(self, cryptokey: CryptoKey) -> NoReturn:
        raise NotImplementedError()

    async def find_by_client_and_is_master(self, client: ClientId, is_master: CryptoKeyIsMaster) -> \
            Tuple[Optional[CryptoKey], Optional[CriteriaQueryMetadata]]:
        raise NotImplementedError()
