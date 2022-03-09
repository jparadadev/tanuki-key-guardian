from src.contexts.backoffice.device.domain.entities.Device import Device
from src.contexts.backoffice.device.domain.entities.DeviceId import DeviceId
from src.contexts.backoffice.device.domain.entities.DeviceName import DeviceName
from src.contexts.backoffice.device.domain.repositories.DeviceRepository import DeviceRepository
from src.contexts.shared.domain.EventBus import EventBus


class DeviceCreator:

    def __init__(self, device_repository: DeviceRepository, event_bus: EventBus):
        self.__device_repository = device_repository
        self.__event_bus = event_bus

    async def run(self, device_id: DeviceId, name: DeviceName):
        device: Device = Device.create(device_id, name)
        await self.__device_repository.create_one(device)
        await self.__event_bus.publish(device.pull_domain_events())
