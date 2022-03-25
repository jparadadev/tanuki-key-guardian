from dependency_injector import containers, providers

from src.apps.backoffice.backend.controllers.ClientDeleteController import ClientDeleteController
from src.apps.backoffice.backend.controllers.ComputedDataGetController import ComputedDataGetController
from src.apps.backoffice.backend.controllers.CryptoKeyPostController import CryptoKeyPostController
from src.apps.backoffice.backend.controllers.CryptoKeysGetController import CryptoKeysGetController
from src.apps.backoffice.backend.controllers.StatusGetController import StatusGetController
from src.apps.backoffice.backend.controllers.ClientsGetController import ClientsGetController
from src.apps.backoffice.backend.controllers.ClientPostController import ClientPostController
from src.contexts.backoffice.clients.application.create_one.CreateClientCommandHandler import CreateClientCommandHandler
from src.contexts.backoffice.clients.application.create_one.ClientCreator import ClientCreator
from src.contexts.backoffice.clients.application.delete_one.ClientDeleter import ClientDeleter
from src.contexts.backoffice.clients.application.delete_one.DeleteClientCommandHandler import DeleteClientCommandHandler
from src.contexts.backoffice.clients.application.findall.ClientsByCriteriaFinder import ClientsByCriteriaFinder
from src.contexts.backoffice.clients.application.findall.FindClientsByCriteriaQueryHandler import \
    FindClientsByCriteriaQueryHandler
from src.contexts.backoffice.clients.infrastructure.persistence.PyMongoClientRepository import PyMongoClientRepository
from src.contexts.backoffice.clients.infrastructure.persistence.config.PyMongoClientConfigFactory import \
    PyMongoClientConfigFactory
from src.contexts.backoffice.computed_data.application.find_one.ComputedDataByKeyAndInputFinder import \
    ComputedDataByKeyAndInputFinder
from src.contexts.backoffice.computed_data.application.find_one.ComputedDataByKeyAndInputQueryHandler import \
    ComputedDataByKeyAndInputQueryHandler
from src.contexts.backoffice.computed_data.infrastructure.persistence.AllAlgorithmComputedDataRepository import \
    AllAlgorithmComputedDataRepository
from src.contexts.backoffice.cryptokeys.application.create_one.CreateCryptoKeyCommandHandler import \
    CreateCryptoKeyCommandHandler
from src.contexts.backoffice.cryptokeys.application.create_one.CryptoKeyCreator import CryptoKeyCreator
from src.contexts.backoffice.cryptokeys.application.findall.CryptoKeysByCriteriaFinder import CryptoKeysByCriteriaFinder
from src.contexts.backoffice.cryptokeys.application.findall.FindCryptoKeysByCriteriaQueryHandler import \
    FindCryptoKeysByCriteriaQueryHandler
from src.contexts.backoffice.cryptokeys.infrastructure.persistence.PyMongoCryptoKeyRepository import \
    PyMongoCryptoKeyRepository
from src.contexts.shared.Infrastructure.commandbus.InMemoryCommandBus import InMemoryCommandBus
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory
from src.contexts.shared.Infrastructure.querybus.InMemoryQueryBus import InMemoryQueryBus


class BackofficeContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(PyMongoClientConfigFactory.create)
    db_client = providers.Singleton(PyMongoClientFactory.create_instance, 'backoffice', db_config)

    client_repository = providers.Singleton(PyMongoClientRepository, db_client)
    cryptokey_repository = providers.Singleton(PyMongoCryptoKeyRepository, db_client)
    computed_data_repository = providers.Singleton(AllAlgorithmComputedDataRepository)

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
    )

    status_get_controller = providers.Singleton(StatusGetController)
    clients_get_controller = providers.Singleton(ClientsGetController, query_bus)
    client_post_controller = providers.Singleton(ClientPostController, command_bus)
    client_delete_controller = providers.Singleton(ClientDeleteController, command_bus)
    cryptokeys_get_controller = providers.Singleton(CryptoKeysGetController, query_bus)
    cryptokeys_post_controller = providers.Singleton(CryptoKeyPostController, command_bus)
    computed_data_get_controller = providers.Singleton(ComputedDataGetController, query_bus)


backoffice_container: BackofficeContainer = BackofficeContainer()


