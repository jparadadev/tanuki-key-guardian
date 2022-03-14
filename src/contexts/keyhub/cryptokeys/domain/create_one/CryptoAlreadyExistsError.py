from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class CryptoKeyAlreadyExistsError(DomainError):

    ERROR_ID = '9cc30b5c-9a36-4a99-a7cd-e342430a3e00'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Crypto Key already exists.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID
