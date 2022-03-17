from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class CryptoKeyInvalidValueError(DomainError):

    ERROR_ID = '5559f4b6-3e6d-4aa9-88fe-65c08472ffc3'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Invalid value for CryptoKey found.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID
