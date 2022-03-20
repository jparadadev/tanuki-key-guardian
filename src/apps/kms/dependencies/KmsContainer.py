from dependency_injector import containers, providers

from src.apps.kms.controllers.ComputedDataGetController import ComputedDataGetController
from src.apps.kms.controllers.CryptoKeyPostController import CryptoKeyPostController
from src.apps.kms.controllers.StatusGetController import StatusGetController
from src.contexts.backoffice.cryptokeys.infrastructure.persistence.PyMongoCryptoKeyRepository import \
    PyMongoCryptoKeyRepository
from src.contexts.backoffice.cryptokeys.infrastructure.persistence.config.PyMongoCryptoKeyConfigFactory import \
    PyMongoCryptoKeyConfigFactory
from src.contexts.kms.computed_data.application.find_one.ComputedDataByKeyAndInputFinder import \
    ComputedDataByKeyAndInputFinder
from src.contexts.kms.computed_data.application.find_one.ComputedDataByKeyAndInputQueryHandler import \
    ComputedDataByKeyAndInputQueryHandler
from src.contexts.kms.computed_data.infrastructure.persistence.AllAlgorithmComputedDataRepository import \
    AllAlgorithmComputedDataRepository
from src.contexts.kms.computed_data.infrastructure.persistence.UselessComputedDataRepository import \
    UselessComputedDataRepository
from src.contexts.kms.cryptokeys.application.create_one.CreateCryptoKeyCommandHandler import \
    CreateCryptoKeyCommandHandler
from src.contexts.kms.cryptokeys.application.create_one.CryptoKeyCreator import CryptoKeyCreator
from src.contexts.shared.Infrastructure.commandbus.InMemoryCommandBus import InMemoryCommandBus
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory
from src.contexts.shared.Infrastructure.querybus.InMemoryQueryBus import InMemoryQueryBus


class KeyhubContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(PyMongoCryptoKeyConfigFactory.create)
    db_client = providers.Singleton(PyMongoClientFactory.create_instance, 'kms', db_config)

    cryptokey_repository = providers.Singleton(PyMongoCryptoKeyRepository, db_client)
    computed_data_repository = providers.Singleton(AllAlgorithmComputedDataRepository)

    cryptokey_creator = providers.Singleton(CryptoKeyCreator, cryptokey_repository, event_bus)
    create_cryptokey_command_handler = providers.Singleton(
        CreateCryptoKeyCommandHandler,
        cryptokey_creator,
    )

    computed_data_by_key_and_input_finder = providers.Singleton(
        ComputedDataByKeyAndInputFinder,
        cryptokey_repository,
        computed_data_repository,
    )
    find_cryptokeys_by_criteria_query_handler = providers.Singleton(
        ComputedDataByKeyAndInputQueryHandler,
        computed_data_by_key_and_input_finder,
    )

    query_bus = providers.Singleton(
        InMemoryQueryBus,
        find_cryptokeys_by_criteria_query_handler,
    )

    command_bus = providers.Singleton(
        InMemoryCommandBus,
        create_cryptokey_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    cryptokeys_post_controller = providers.Singleton(CryptoKeyPostController, command_bus)
    computed_data_get_controller = providers.Singleton(ComputedDataGetController, query_bus)


computed_data_container: KeyhubContainer = KeyhubContainer()


