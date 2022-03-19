from dependency_injector import containers, providers

from src.apps.ca.controllers.CryptoKeysGetController import CryptoKeysGetController
from src.apps.ca.controllers.StatusGetController import StatusGetController
from src.contexts.kms.cryptokeys.application.find_all_not_private.CryptoKeysByCriteriaAndNotPrivateFinder import CryptoKeysByCriteriaAndNotPrivateFinder
from src.contexts.kms.cryptokeys.application.find_all_not_private.FindCryptoKeysByCriteriaAndNotPrivateQueryHandler import \
    FindCryptoKeysByCriteriaAndNotPrivateQueryHandler
from src.contexts.ca.cryptokeys.infrastructure.persistence.PyMongoCryptoKeyRepository import \
    PyMongoCryptoKeyRepository
from src.contexts.ca.cryptokeys.infrastructure.persistence.config.PyMongoCryptoKeyConfigFactory import \
    PyMongoCryptoKeyConfigFactory
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory
from src.contexts.shared.Infrastructure.querybus.InMemoryQueryBus import InMemoryQueryBus


class CaContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(PyMongoCryptoKeyConfigFactory.create)
    db_client = providers.Singleton(PyMongoClientFactory.create_instance, 'ca', db_config)

    client_repository = providers.Singleton(PyMongoCryptoKeyRepository, db_client)
    cryptokey_repository = providers.Singleton(PyMongoCryptoKeyRepository, db_client)

    cryptokeys_by_criteria_finder = providers.Singleton(CryptoKeysByCriteriaAndNotPrivateFinder, cryptokey_repository)
    find_cryptokeys_by_criteria_query_handler = providers.Singleton(
        FindCryptoKeysByCriteriaAndNotPrivateQueryHandler,
        cryptokeys_by_criteria_finder,
    )

    query_bus = providers.Singleton(
        InMemoryQueryBus,
        find_cryptokeys_by_criteria_query_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    cryptokeys_get_controller = providers.Singleton(CryptoKeysGetController, query_bus)


ca_container: CaContainer = CaContainer()


