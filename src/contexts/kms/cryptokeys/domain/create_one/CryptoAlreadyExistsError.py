from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class CryptoKeyAlreadyExistsError(DomainError):
    ERROR_ID = '9d45faad-9d21-462a-a51f-3d3070bcf2da'

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
