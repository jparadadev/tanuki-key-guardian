from src.contexts.backoffice.devices.application.findall.BackofficeDevicesResponse import BackofficeDevicesResponse
from src.contexts.backoffice.devices.domain.repositories.DeviceRepository import DeviceRepository
from src.contexts.shared.domain.criteria.Criteria import Criteria


class DevicesByCriteriaFinder:

    def __init__(self, device_repository: DeviceRepository):
        self._device_repository = device_repository

    async def run(self, criteria: Criteria) -> BackofficeDevicesResponse:
        devices, criteria_metadata = await self._device_repository.find_by_criteria(criteria)
        return BackofficeDevicesResponse(devices, criteria_metadata)

