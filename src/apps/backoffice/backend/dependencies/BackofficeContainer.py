from dependency_injector import containers, providers

from src.apps.backoffice.backend.controllers.StatusGetController import StatusGetController
from src.apps.backoffice.backend.controllers.DevicesGetController import DevicesGetController
from src.apps.backoffice.backend.controllers.DevicePostController import DevicePostController
from src.contexts.backoffice.devices.application.create_one.CreateDeviceCommandHandler import CreateDeviceCommandHandler
from src.contexts.backoffice.devices.application.create_one.DeviceCreator import DeviceCreator
from src.contexts.backoffice.devices.application.findall.DevicesByCriteriaFinder import DevicesByCriteriaFinder
from src.contexts.backoffice.devices.application.findall.FindDevicesByCriteriaQueryHandler import \
    FindDevicesByCriteriaQueryHandler
from src.contexts.backoffice.devices.infrastructure.persistence.PyMongoDeviceRepository import PyMongoDeviceRepository
from src.contexts.backoffice.devices.infrastructure.persistence.config.PyMongoDeviceConfigFactory import \
    PyMongoDeviceConfigFactory
from src.contexts.shared.Infrastructure.commandbus.InMemoryCommandBus import InMemoryCommandBus
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory
from src.contexts.shared.Infrastructure.querybus.InMemoryQueryBus import InMemoryQueryBus


class BackofficeContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(PyMongoDeviceConfigFactory.create)
    db_client = providers.Singleton(PyMongoClientFactory.create_instance, 'backoffice', db_config)

    device_repository = providers.Singleton(PyMongoDeviceRepository, db_client)

    devices_by_criteria_finder = providers.Singleton(DevicesByCriteriaFinder, device_repository)
    find_devices_by_criteria_query_handler = providers.Singleton(
        FindDevicesByCriteriaQueryHandler,
        devices_by_criteria_finder,
    )

    device_creator = providers.Singleton(DeviceCreator, device_repository, event_bus)
    create_device_command_handler = providers.Singleton(
        CreateDeviceCommandHandler,
        device_creator,
    )

    query_bus = providers.Singleton(
        InMemoryQueryBus,
        find_devices_by_criteria_query_handler,
    )

    command_bus = providers.Singleton(
        InMemoryCommandBus,
        create_device_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    devices_get_controller = providers.Singleton(DevicesGetController, query_bus)
    device_post_controller = providers.Singleton(DevicePostController, command_bus)


backoffice_container: BackofficeContainer = BackofficeContainer()


