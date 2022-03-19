from typing import Dict, Any

from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.kms.controllers.KmsController import KmsController
from src.contexts.backoffice.cryptokeys.application.create_one.CreateCryptoKeyCommand import CreateCryptoKeyCommand
from src.contexts.backoffice.cryptokeys.infrastructure.CryptoKeysHttpResponseErrorHandler import \
    JsonResponseErrorHandler
from src.contexts.kms.computed_data.application.find_one.ComputedDataByKeyAndInputQuery import \
    ComputedDataByKeyAndInputQuery
from src.contexts.shared.Infrastructure.parsers.parse_dict_format_to_criteria import parse_dict_to_criteria
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.QueryBus import QueryBus
from src.contexts.shared.domain.errors.DomainError import DomainError


class ComputedDataGetController(KmsController):

    def __init__(
            self,
            query_bus: QueryBus,
    ):
        self._query_bus = query_bus
        self._error_handler = JsonResponseErrorHandler()

    async def run(self, req: Request) -> JSONResponse:
        query_params = dict(req.query_params)

        query: ComputedDataByKeyAndInputQuery = ComputedDataByKeyAndInputQuery(query_params.get('key-id'),
                                                                               query_params.get('input'))
        try:
            content = await self._query_bus.ask(query)
        except DomainError as err:
            return self._error_handler.resolve(err)

        return JSONResponse(status_code=HTTPStatus.OK, content=content.to_primitives())
