from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class CryptoKeyIsMaster(ValueObject):

    def __init__(self, value: bool):
        super().__init__(value)
