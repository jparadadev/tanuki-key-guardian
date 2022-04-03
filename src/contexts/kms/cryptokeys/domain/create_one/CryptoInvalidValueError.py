from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class CryptoKeyInvalidValueError(DomainError):
    ERROR_ID = '8fd818c5-10dc-4639-82ac-d4b37394517d'

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
