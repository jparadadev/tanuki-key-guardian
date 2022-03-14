from dependency_injector import containers, providers

from src.apps.keyhub.controllers.CryptoKeyPostController import CryptoKeyPostController
from src.apps.keyhub.controllers.StatusGetController import StatusGetController
from src.contexts.keyhub.cryptokeys.application.create_one.CreateCryptoKeyCommandHandler import \
    CreateCryptoKeyCommandHandler
from src.contexts.keyhub.cryptokeys.application.create_one.CryptoKeyCreator import CryptoKeyCreator
from src.contexts.keyhub.cryptokeys.infrastructure.persistence.PyMongoCryptoKeyRepository import \
    PyMongoCryptoKeyRepository
from src.contexts.keyhub.cryptokeys.infrastructure.persistence.config.PyMongoCryptoKeyConfigFactory import \
    PyMongoCryptoKeyConfigFactory
from src.contexts.shared.Infrastructure.commandbus.InMemoryCommandBus import InMemoryCommandBus
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory
from src.contexts.shared.Infrastructure.querybus.InMemoryQueryBus import InMemoryQueryBus


class KeyhubContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(PyMongoCryptoKeyConfigFactory.create)
    db_client = providers.Singleton(PyMongoClientFactory.create_instance, 'keyhub', db_config)

    cryptokey_repository = providers.Singleton(PyMongoCryptoKeyRepository, db_client)

    cryptokey_creator = providers.Singleton(CryptoKeyCreator, cryptokey_repository, event_bus)
    create_cryptokey_command_handler = providers.Singleton(
        CreateCryptoKeyCommandHandler,
        cryptokey_creator,
    )

    query_bus = providers.Singleton(
        InMemoryQueryBus,
    )

    command_bus = providers.Singleton(
        InMemoryCommandBus,
        create_cryptokey_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    cryptokeys_post_controller = providers.Singleton(CryptoKeyPostController, command_bus)


keyhub_container: KeyhubContainer = KeyhubContainer()


