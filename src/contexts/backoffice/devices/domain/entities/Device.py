from datetime import datetime
from typing import Dict, List, Union, Any

from src.contexts.backoffice.device.domain.domainevents.DeviceCreatedDomainEvent import DeviceCreatedDomainEvent
from src.contexts.backoffice.device.domain.entities.DeviceCreationDate import DeviceCreationDate
from src.contexts.backoffice.device.domain.entities.DeviceId import DeviceId
from src.contexts.backoffice.device.domain.entities.DeviceName import DeviceName
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class Device(AggregateRoot):

    def __init__(self, device_id: DeviceId, name: DeviceName, created_at: DeviceCreationDate):
        super().__init__()
        self.id = device_id
        self.name = name
        self.created_at = created_at

    @staticmethod
    def create(device_id: DeviceId, name: DeviceName):
        now = DeviceCreationDate(datetime.now())
        device = Device(device_id, name, now)
        event = DeviceCreatedDomainEvent(device.id.value(), device)
        device.record_event(event)
        return device

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        device = Device(
            DeviceId(raw_data.get('id')),
            DeviceName(raw_data.get('name')),
            DeviceCreationDate(raw_data.get('created-at')),
        )
        return device

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'name': self.name.value(),
            'created-at': self.created_at.value(),
        }
