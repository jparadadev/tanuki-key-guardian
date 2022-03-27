from typing import Any, Dict, List

from src.contexts.backoffice.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.backoffice.computed_data.domain.entities.ComputedDataMeta import ComputedDataMeta
from src.contexts.backoffice.computed_data.domain.entities.ComputedDataOutput import ComputedDataOutput
from src.contexts.backoffice.computed_data.domain.entities.ComputedDataType import ComputedDataType
from src.contexts.kms.cryptokeys.domain.entities.CryptoKeyId import CryptoKeyId
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class ComputedData(AggregateRoot):

    def __init__(self, cd_input: ComputedDataInput, cd_output: ComputedDataOutput, key_id: CryptoKeyId,
                 cd_type: ComputedDataType, meta: ComputedDataMeta):
        super().__init__()
        self.cd_input = cd_input
        self.cd_output = cd_output
        self.key_id = key_id
        self.type = cd_type
        self.meta = meta

    @staticmethod
    def create(cd_input: ComputedDataInput, cd_output: ComputedDataOutput, key_id: CryptoKeyId,
               cd_type: ComputedDataType, meta: ComputedDataMeta):
        computed_data = ComputedData(cd_input, cd_output, key_id, cd_type, meta)
        return computed_data

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        client = ComputedData(
            ComputedDataInput(raw_data.get('input')),
            ComputedDataOutput(raw_data.get('output')),
            CryptoKeyId(raw_data.get('key_id')),
            ComputedDataType(raw_data.get('type')),
            ComputedDataMeta(raw_data.get('meta')),
        )
        return client

    def to_primitives(self) -> Dict or List:
        return {
            'input': self.cd_input.value(),
            'output': self.cd_output.value(),
            'key_id': self.key_id.value(),
            'type': self.type.value(),
            'meta': self.meta.value(),
        }
