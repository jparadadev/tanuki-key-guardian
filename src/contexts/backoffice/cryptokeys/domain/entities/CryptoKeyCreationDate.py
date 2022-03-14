from datetime import datetime

from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class CryptoKeyCreationDate(ValueObject):

    def __init__(self, value: datetime):
        super().__init__(value)

    def value(self) -> datetime:
        return self._value
