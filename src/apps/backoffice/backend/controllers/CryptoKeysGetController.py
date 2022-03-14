from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.backoffice.backend.controllers.BackofficeController import BackofficeController

from src.contexts.backoffice.cryptokeys.application.findall.FindCryptoKeysByCriteriaQuery import \
    FindCryptoKeysByCriteriaQuery
from src.contexts.shared.Infrastructure.parsers.parse_dict_format_to_criteria import parse_dict_to_criteria
from src.contexts.shared.domain.Response import Response
from src.contexts.shared.domain.Query import Query
from src.contexts.shared.domain.QueryBus import QueryBus
from fastapi.encoders import jsonable_encoder


class CryptoKeysGetController(BackofficeController):

    def __init__(
            self,
            query_bus: QueryBus,
    ):
        self._query_bus = query_bus

    async def run(self, req: Request) -> JSONResponse:
        query_params = dict(req.query_params)
        filters, order_by, limit = parse_dict_to_criteria(query_params)
        query: Query = FindCryptoKeysByCriteriaQuery(filters, order_by, limit)
        res: Response = await self._query_bus.ask(query)
        json_compatible_item_data = jsonable_encoder(res.to_primitives())
        return JSONResponse(status_code=HTTPStatus.OK, content=json_compatible_item_data)
