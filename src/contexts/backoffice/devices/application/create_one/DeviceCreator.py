from src.contexts.backoffice.devices.domain.entities.Device import Device
from src.contexts.backoffice.devices.domain.entities.DeviceId import DeviceId
from src.contexts.backoffice.devices.domain.entities.DeviceName import DeviceName
from src.contexts.backoffice.devices.domain.repositories.DeviceRepository import DeviceRepository
from src.contexts.shared.domain.EventBus import EventBus


class DeviceCreator:

    def __init__(self, device_repository: DeviceRepository, event_bus: EventBus):
        self._device_repository = device_repository
        self._event_bus = event_bus

    async def run(self, device_id: DeviceId, name: DeviceName):
        device: Device = Device.create(device_id, name)
        await self._device_repository.create_one(device)
        await self._event_bus.publish(device.pull_domain_events())
