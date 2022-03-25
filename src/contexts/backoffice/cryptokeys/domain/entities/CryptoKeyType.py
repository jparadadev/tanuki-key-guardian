from enum import Enum

from src.contexts.backoffice.cryptokeys.domain.create_one.CryptoInvalidValueError import CryptoKeyInvalidValueError
from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class CryptoKeyTypes(Enum):

    RSA = 'rsa'
    DIFFIE_HELLMAN = 'diffie-hellman'
    DIFFIE_HELLMAN_ELLIPTIC_CURVE = 'diffie-hellman-elliptic-curve'
    DIFFIE_HELLMAN_HMAC = 'diffie-hellman-hmac'
    DES = 'des'
    AES = 'aes'

    @classmethod
    def has_value(cls, value):
        values = [item.value for item in CryptoKeyTypes]
        return value in values

    @classmethod
    def get_values(cls):
        return [item.value for item in CryptoKeyTypes]


class CryptoKeyType(ValueObject):

    def __init__(self, value: str):
        super().__init__(value)
        if not CryptoKeyTypes.has_value(value):
            raise CryptoKeyInvalidValueError(f'Invalid value for <{value}>. '
                                             f'Should be one of <{CryptoKeyTypes.get_values()}>.')

