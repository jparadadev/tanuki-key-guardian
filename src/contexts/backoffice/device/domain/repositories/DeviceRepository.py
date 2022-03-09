from abc import ABC
from typing import List, NoReturn, Tuple, Optional

from src.contexts.backoffice.device.domain.entities.Device import Device
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class DeviceRepository(ABC):

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[Device], Optional[CriteriaQueryMetadata]]:
        raise NotImplementedError()

    async def create_one(self, device: Device) -> NoReturn:
        raise NotImplementedError()
