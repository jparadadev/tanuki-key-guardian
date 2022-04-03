from http import HTTPStatus
from typing import Any, Dict

from starlette.responses import JSONResponse

from src.contexts.kms.clients.domain.create_one.ClientAlreadyExistsError import ClientAlreadyExistsError
from src.contexts.kms.clients.domain.create_one.ClientInvalidValueError import ClientInvalidValueError
from src.contexts.kms.clients.domain.find_one.ClientNotFoundError import ClientNotFoundError
from src.contexts.shared.domain.errors.DomainError import DomainError


class JsonResponseErrorHandler:
    _ERROR_OPTIONS_MAPPING: Dict[str, Dict[str, Any]] = {
        ClientAlreadyExistsError.ERROR_ID: {
            'is-private': False,
            'is-critical': False,
            'status-code': HTTPStatus.CONFLICT,
        },
        ClientInvalidValueError.ERROR_ID: {
            'is-private': False,
            'is-critical': False,
            'status-code': HTTPStatus.BAD_REQUEST,
        },
        ClientNotFoundError.ERROR_ID: {
            'is-private': False,
            'is-critical': False,
            'status-code': HTTPStatus.NOT_FOUND,
        }
    }

    def __init__(self):
        pass

    def resolve(self, error: DomainError) -> JSONResponse:
        error_options = None
        for error_id, options in self._ERROR_OPTIONS_MAPPING.items():
            if error_id == error.get_id():
                error_options = options
                break
        if error_options is not None:
            status = error_options['status-code']
            content = error.to_primitives()
            if error_options['is-private']:
                del content['message']
            response = JSONResponse(
                status_code=status,
                content=content,
            )
            return response

        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
