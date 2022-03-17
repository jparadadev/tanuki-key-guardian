from abc import ABC
from typing import List, Tuple, Optional

from src.contexts.ca.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class CryptoKeyRepository(ABC):

    async def find_by_criteria_and_is_not_private(self, criteria: Criteria) -> Tuple[List[CryptoKey],
                                                                                     Optional[CriteriaQueryMetadata]]:
        raise NotImplementedError()
