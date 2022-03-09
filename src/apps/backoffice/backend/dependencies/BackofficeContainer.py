from dependency_injector import containers, providers

from src.apps.backoffice.backend.controllers.StatusGetController import StatusGetController
from src.apps.backoffice.backend.controllers.ClientsGetController import ClientsGetController
from src.apps.backoffice.backend.controllers.ClientPostController import ClientPostController
from src.contexts.backoffice.clients.application.create_one.CreateClientCommandHandler import CreateClientCommandHandler
from src.contexts.backoffice.clients.application.create_one.ClientCreator import ClientCreator
from src.contexts.backoffice.clients.application.findall.ClientsByCriteriaFinder import ClientsByCriteriaFinder
from src.contexts.backoffice.clients.application.findall.FindClientsByCriteriaQueryHandler import \
    FindClientsByCriteriaQueryHandler
from src.contexts.backoffice.clients.infrastructure.persistence.PyMongoClientRepository import PyMongoClientRepository
from src.contexts.backoffice.clients.infrastructure.persistence.config.PyMongoClientConfigFactory import \
    PyMongoClientConfigFactory
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

    clients_by_criteria_finder = providers.Singleton(ClientsByCriteriaFinder, client_repository)
    find_clients_by_criteria_query_handler = providers.Singleton(
        FindClientsByCriteriaQueryHandler,
        clients_by_criteria_finder,
    )

    client_creator = providers.Singleton(ClientCreator, client_repository, event_bus)
    create_client_command_handler = providers.Singleton(
        CreateClientCommandHandler,
        client_creator,
    )

    query_bus = providers.Singleton(
        InMemoryQueryBus,
        find_clients_by_criteria_query_handler,
    )

    command_bus = providers.Singleton(
        InMemoryCommandBus,
        create_client_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    clients_get_controller = providers.Singleton(ClientsGetController, query_bus)
    client_post_controller = providers.Singleton(ClientPostController, command_bus)


backoffice_container: BackofficeContainer = BackofficeContainer()


