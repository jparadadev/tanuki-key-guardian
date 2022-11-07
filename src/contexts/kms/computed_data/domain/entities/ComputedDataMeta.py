from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class ComputedDataMeta(ValueObject):

    def __init__(self, value: dict):
        if value is None:
            value = {}
        super().__init__(value)
