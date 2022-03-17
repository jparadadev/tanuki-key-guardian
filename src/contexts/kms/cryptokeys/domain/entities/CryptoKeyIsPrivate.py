from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class CryptoKeyIsPrivate(ValueObject):

    def __init__(self, value: bool):
        super().__init__(value)
