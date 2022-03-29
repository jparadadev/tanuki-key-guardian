from typing import List, NoReturn, Tuple, Optional

from src.contexts.kms.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.kms.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.Interface import Interface
from src.contexts.shared.domain.criteria.Criteria import Criteria


class CryptoKeyRepository(Interface):

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[CryptoKey], Optional[CriteriaQueryMetadata]]:
        raise NotImplementedError()

    async def find_by_id(self, key_id: CryptoKeyId) -> Optional[CryptoKey]:
        raise NotImplementedError()

    async def create_one(self, cryptokey: CryptoKey) -> NoReturn:
        raise NotImplementedError()

    async def update_one(self, cryptokey: CryptoKey) -> NoReturn:
        raise NotImplementedError()
