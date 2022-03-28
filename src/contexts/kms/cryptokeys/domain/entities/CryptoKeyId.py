from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class CryptoKeyId(ValueObject):

    def __init__(self, value: str):
        super().__init__(value)
