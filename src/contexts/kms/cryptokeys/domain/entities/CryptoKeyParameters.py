from typing import Any

from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class CryptoKeyParameters(ValueObject):

    def __init__(self, value: Any):
        super().__init__(value)
