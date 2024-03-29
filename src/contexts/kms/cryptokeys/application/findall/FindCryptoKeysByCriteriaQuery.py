from typing import List

from src.contexts.shared.domain.Query import Query
from src.contexts.shared.domain.criteria.Filter import Filter
from src.contexts.shared.domain.criteria.Limit import Limit
from src.contexts.shared.domain.criteria.OrderBy import OrderBy


class FindCryptoKeysByCriteriaQuery(Query):
    QUERY_TYPE: str = 'kms.cryptokey.find-by-criteria'

    def __init__(
            self,
            filters: List[Filter],
            order_by: OrderBy = None,
            limit: Limit = None,
    ):
        self.filters = filters
        self.order_by = order_by
        self.limit = limit

    def get_query_type_name(self) -> str:
        return self.QUERY_TYPE
