from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class CryptoKeyNotFoundError(DomainError):
    ERROR_ID = '65f403a5-a6f2-412b-bbcd-356142927888'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Crypto Key not found.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID
