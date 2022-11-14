from dependency_injector import containers, providers

from src.apps.kms.backend.controllers.client.ClientDeleteController import ClientDeleteController
from src.apps.kms.backend.controllers.client.ClientPostController import ClientPostController
from src.apps.kms.backend.controllers.client.ClientsGetController import ClientsGetController
from src.apps.kms.backend.controllers.computed_data.ComputedDataGetController import ComputedDataGetController
from src.apps.kms.backend.controllers.crypto_key.CryptoKeyPostController import CryptoKeyPostController
from src.apps.kms.backend.controllers.crypto_key.CryptoKeysGetController import CryptoKeysGetController
from src.apps.kms.backend.controllers.crypto_key.RotateCryptoKeyPutController import RotateCryptoKeyPutController
from src.apps.kms.backend.controllers.health.StatusGetController import StatusGetController
from src.contexts.kms.clients.application.create_one.ClientCreator import ClientCreator
from src.contexts.kms.clients.application.create_one.CreateClientCommandHandler import CreateClientCommandHandler
from src.contexts.kms.clients.application.delete_one.ClientDeleter import ClientDeleter
from src.contexts.kms.clients.application.delete_one.DeleteClientCommandHandler import DeleteClientCommandHandler
from src.contexts.kms.clients.application.findall.ClientsByCriteriaFinder import ClientsByCriteriaFinder
from src.contexts.kms.clients.application.findall.FindClientsByCriteriaQueryHandler import \
    FindClientsByCriteriaQueryHandler
from src.contexts.kms.clients.infrastructure.persistence.PyMongoClientRepository import PyMongoClientRepository
from src.contexts.kms.clients.infrastructure.persistence.config.PyMongoClientConfigFactory import \
    PyMongoClientConfigFactory
from src.contexts.kms.computed_data.application.find_one.ComputedDataByKeyAndInputFinder import \
    ComputedDataByKeyAndInputFinder
from src.contexts.kms.computed_data.application.find_one.ComputedDataByKeyAndInputQueryHandler import \
    ComputedDataByKeyAndInputQueryHandler
from src.contexts.kms.computed_data.domain.repositories.ComputedDataRepository import ComputedDataRepository
from src.contexts.kms.computed_data.infrastructure.persistence.UselessComputedDataRepository import \
    UselessComputedDataRepository
from src.contexts.kms.cryptokeys.application.create_one.CreateCryptoKeyCommandHandler import \
    CreateCryptoKeyCommandHandler
from src.contexts.kms.cryptokeys.application.create_one.CryptoKeyCreator import CryptoKeyCreator
from src.contexts.kms.cryptokeys.application.findall.CryptoKeysByCriteriaFinder import CryptoKeysByCriteriaFinder
from src.contexts.kms.cryptokeys.application.findall.FindCryptoKeysByCriteriaQueryHandler import \
    FindCryptoKeysByCriteriaQueryHandler
from src.contexts.kms.cryptokeys.application.rotate_one.CryptoKeyRotator import CryptoKeyRotator
from src.contexts.kms.cryptokeys.application.rotate_one.RotateCryptoKeyCommandHandler import \
    RotateCryptoKeyCommandHandler
from src.contexts.kms.cryptokeys.infrastructure.persistence.PyMongoCryptoKeyRepository import \
    PyMongoCryptoKeyRepository
from src.contexts.shared.Infrastructure.commandbus.InMemoryCommandBus import InMemoryCommandBus
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory
from src.contexts.shared.Infrastructure.querybus.InMemoryQueryBus import InMemoryQueryBus


class KmsContainer(containers.DeclarativeContainer):
    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(PyMongoClientConfigFactory.create)
    db_client = providers.Singleton(PyMongoClientFactory.create_instance, 'kms', db_config)

    client_repository = providers.Singleton(PyMongoClientRepository, db_client)
    cryptokey_repository = providers.Singleton(PyMongoCryptoKeyRepository, db_client)
    computed_data_repository = providers.Singleton(ComputedDataRepository)

    clients_by_criteria_finder = providers.Singleton(ClientsByCriteriaFinder, client_repository)
    find_clients_by_criteria_query_handler = providers.Singleton(
        FindClientsByCriteriaQueryHandler,
        clients_by_criteria_finder,
    )

    cryptokeys_by_criteria_finder = providers.Singleton(CryptoKeysByCriteriaFinder, cryptokey_repository)
    find_cryptokeys_by_criteria_query_handler = providers.Singleton(
        FindCryptoKeysByCriteriaQueryHandler,
        cryptokeys_by_criteria_finder,
    )

    client_creator = providers.Singleton(ClientCreator, client_repository, event_bus)
    create_client_command_handler = providers.Singleton(
        CreateClientCommandHandler,
        client_creator,
    )

    client_deleter = providers.Singleton(ClientDeleter, client_repository, event_bus)
    delete_client_command_handler = providers.Singleton(
        DeleteClientCommandHandler,
        client_deleter,
    )

    cryptokey_creator = providers.Singleton(CryptoKeyCreator, cryptokey_repository, event_bus)
    create_cryptokey_command_handler = providers.Singleton(
        CreateCryptoKeyCommandHandler,
        cryptokey_creator,
    )

    cryptokey_rotator = providers.Singleton(CryptoKeyRotator, cryptokey_repository, event_bus)
    rotate_cryptokey_command_handler = providers.Singleton(
        RotateCryptoKeyCommandHandler,
        cryptokey_rotator,
    )

    computed_data_by_key_and_input_finder = providers.Singleton(
        ComputedDataByKeyAndInputFinder,
        cryptokey_repository,
        computed_data_repository,
    )
    find_computed_data_by_criteria_query_handler = providers.Singleton(
        ComputedDataByKeyAndInputQueryHandler,
        computed_data_by_key_and_input_finder,
    )

    query_bus = providers.Singleton(
        InMemoryQueryBus,
        find_clients_by_criteria_query_handler,
        find_cryptokeys_by_criteria_query_handler,
        find_computed_data_by_criteria_query_handler,
    )

    command_bus = providers.Singleton(
        InMemoryCommandBus,
        create_client_command_handler,
        create_cryptokey_command_handler,
        delete_client_command_handler,
        rotate_cryptokey_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    clients_get_controller = providers.Singleton(ClientsGetController, query_bus)
    client_post_controller = providers.Singleton(ClientPostController, command_bus)
    client_delete_controller = providers.Singleton(ClientDeleteController, command_bus)
    cryptokeys_get_controller = providers.Singleton(CryptoKeysGetController, query_bus)
    cryptokeys_post_controller = providers.Singleton(CryptoKeyPostController, command_bus)
    rotate_cryptokey_put_controller = providers.Singleton(RotateCryptoKeyPutController, command_bus)
    computed_data_get_controller = providers.Singleton(ComputedDataGetController, query_bus)


kms_container: KmsContainer = KmsContainer()
