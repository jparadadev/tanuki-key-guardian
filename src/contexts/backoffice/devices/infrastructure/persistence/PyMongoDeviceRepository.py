from typing import List, NoReturn, Tuple, Optional

from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError

from src.contexts.backoffice.devices.domain.entities.Device import Device
from src.contexts.backoffice.devices.domain.create_one.DeviceAlreadyExistsError import DeviceAlreadyExistsError
from src.contexts.backoffice.devices.domain.repositories.DeviceRepository import DeviceRepository
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoRepository import PyMongoRepository
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class PyMongoDeviceRepository(PyMongoRepository, DeviceRepository):

    _COLLECTION_NAME = 'devices'
    _DATABASE_NAME = 'tanuki-key-guardian'

    def __init__(self, client: MongoClient):
        super().__init__(client)
        super()._get_collection().create_index([
            ('id', ASCENDING)
        ], unique=True)

    def get_database_name(self):
        return self._DATABASE_NAME

    def get_collection_name(self):
        return self._COLLECTION_NAME

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[Device], Optional[CriteriaQueryMetadata]]:
        results, count = await super()._find_by_criteria(criteria)
        entities = [Device.create_from_primitives(result) for result in results]
        metadata = CriteriaQueryMetadata(count)
        return entities, metadata

    async def create_one(self, device: Device) -> NoReturn:
        try:
            device = await super()._create_one(device.to_primitives())
            return device
        except DuplicateKeyError as _:
            raise DeviceAlreadyExistsError('Device with ID <{}> already exists.'.format(device.id.value()))
