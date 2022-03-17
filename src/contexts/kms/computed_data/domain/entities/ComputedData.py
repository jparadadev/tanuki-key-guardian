from typing import Any

from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.kms.computed_data.domain.entities.ComputedDataOutput import ComputedDataOutput
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class ComputedData(AggregateRoot):

    def __init__(self, cd_input: ComputedDataInput, cd_output: ComputedDataOutput, key_id: CryptoKeyId):
        super().__init__()
        self.cd_input = cd_input
        self.cd_output = cd_output
        self.key_id = key_id

    @staticmethod
    def create(cd_input: ComputedDataInput, cd_output: ComputedDataOutput, key_id: CryptoKeyId):
        computed_data = ComputedData(cd_input, cd_output, key_id)
        return computed_data

    @staticmethod
    def create_from_primitives(raw_data: dict[str, Any]):
        client = ComputedData(
            ComputedDataInput(raw_data.get('input')),
            ComputedDataOutput(raw_data.get('output')),
            CryptoKeyId(raw_data.get('key_id')),
        )
        return client

    def to_primitives(self) -> dict or list:
        return {
            'input': self.cd_input.value(),
            'output': self.cd_output.value(),
            'key_id': self.key_id.value(),
        }
