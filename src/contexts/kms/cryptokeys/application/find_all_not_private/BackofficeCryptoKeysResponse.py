from typing import List, Any

from src.contexts.ca.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.shared.domain.Metadata import Metadata
from src.contexts.shared.domain.Response import Response


class BackofficeCryptoKeysResponse(Response):

    def __init__(
            self,
            cryptokeys: List[CryptoKey],
            metadata: Metadata = None,
    ):
        self._cryptokeys = cryptokeys
        self._meta = metadata

    def to_primitives(self) -> Any:
        json_cryptokeys = [cryptokey.to_primitives() for cryptokey in self._cryptokeys]
        response = {
            'data': json_cryptokeys,
        }
        if self._meta is not None:
            response['metadata'] = self._meta.to_dict()
        return response
