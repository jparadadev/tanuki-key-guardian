from enum import Enum

from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class ComputedDataTypes(Enum):
    ENCRYPT = 'encrypt'
    DECRYPT = 'decrypt'
    KEY_EXCHANGE = 'key-exchange'

    @classmethod
    def has_value(cls, value):
        values = [item.value for item in ComputedDataTypes]
        return value in values

    @classmethod
    def get_values(cls):
        return [item.value for item in ComputedDataTypes]


class ComputedDataType(ValueObject):

    def __init__(self, value: str):
        super().__init__(value)
