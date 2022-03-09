from enum import Enum

from src.contexts.shared.domain.errors.ValueObjectValidationError import ValueObjectValidationError


class OrderDirectionValues(Enum):
    ASC = 'asc'
    DESC = 'desc'


class OrderDirection:

    _allowed_values = [e.value for e in OrderDirectionValues]

    def __init__(self, order_dir: str):
        if order_dir not in self._allowed_values:
            raise ValueObjectValidationError('Order direction must be one of {} but {} found.'
                                             .format(self._allowed_values, order_dir))
        self.value = order_dir
