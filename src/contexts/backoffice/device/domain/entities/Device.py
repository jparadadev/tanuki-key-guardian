from typing import Dict, List, Union, Any

from src.contexts.backoffice.device.domain.domainevents.DeviceCreatedDomainEvent import DeviceCreatedDomainEvent
from src.contexts.backoffice.device.domain.entities.DeviceCreationDate import DeviceName
from src.contexts.backoffice.device.domain.entities.DeviceId import DeviceId
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class Device(AggregateRoot):

    def __init__(self, device_id: DeviceId, name: DeviceName):
        super().__init__()
        self.id = device_id
        self.name = name

    @staticmethod
    def create(device_id: DeviceId, name: DeviceName):
        device = Device(device_id, name)
        event = DeviceCreatedDomainEvent(device.id.value(), device)
        device.record_event(event)
        return device

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        device = Device(
            DeviceId(raw_data.get('id')),
            DeviceName(raw_data.get('name')),
        )
        return device

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'name': self.name.value(),
        }
