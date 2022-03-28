from http import HTTPStatus
from typing import Any, Dict

from starlette.responses import JSONResponse

from src.contexts.kms.cryptokeys.domain.create_one.CryptoAlreadyExistsError import CryptoKeyAlreadyExistsError
from src.contexts.kms.cryptokeys.domain.create_one.CryptoInvalidValueError import CryptoKeyInvalidValueError
from src.contexts.kms.cryptokeys.domain.find_one.CryptoKeyNotFoundError import CryptoKeyNotFoundError
from src.contexts.shared.domain.errors.DomainError import DomainError


class JsonResponseErrorHandler:

    _ERROR_OPTIONS_MAPPING: Dict[str, Dict[str, Any]] = {
        CryptoKeyAlreadyExistsError.ERROR_ID: {
            'is-private': False,
            'is-critical': False,
            'status-code': HTTPStatus.CONFLICT,
        },
        CryptoKeyInvalidValueError.ERROR_ID: {
            'is-private': False,
            'is-critical': False,
            'status-code': HTTPStatus.BAD_REQUEST,
        },
        CryptoKeyNotFoundError.ERROR_ID: {
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
