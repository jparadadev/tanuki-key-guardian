from typing import Any

from src.contexts.kms.computed_data.domain.entities.ComputedData import ComputedData
from src.contexts.shared.domain.Response import Response


class KmsComputedDataResponse(Response):

    def __init__(
            self,
            computed_data: ComputedData
    ):
        self._computed_data = computed_data

    def to_primitives(self) -> Any:
        json_computed_data = self._computed_data.to_primitives()
        response = {
            'data': json_computed_data,
        }
        return response
