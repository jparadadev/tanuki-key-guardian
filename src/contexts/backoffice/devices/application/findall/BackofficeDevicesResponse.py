from typing import List, Any

from src.contexts.backoffice.devices.domain.entities.Device import Device
from src.contexts.shared.domain.Metadata import Metadata
from src.contexts.shared.domain.Response import Response


class BackofficeDevicesResponse(Response):

    def __init__(
            self,
            devices: List[Device],
            metadata: Metadata = None,
    ):
        self._devices = devices
        self._meta = metadata

    def to_primitives(self) -> Any:
        json_users = [user.to_primitives() for user in self._devices]
        response = {
            'data': json_users,
        }
        if self._meta is not None:
            response['metadata'] = self._meta.to_dict()
        return response
