from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class ComputedDataMeta(ValueObject):

    def __init__(self, value: dict):
        super().__init__(value)
