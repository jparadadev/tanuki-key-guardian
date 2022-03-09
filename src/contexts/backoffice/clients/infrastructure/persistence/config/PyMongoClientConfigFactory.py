from src.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from src.contexts.shared.Infrastructure.environment.EnvVar import EnvVar
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoConfiguration import PyMongoConfiguration


class PyMongoClientConfigFactory:

    @staticmethod
    def create() -> PyMongoConfiguration:
        config = PyMongoConfiguration(
            EnvManager.get(EnvVar.SHARED_CLIENT_MONGO_HOST),
            EnvManager.get(EnvVar.SHARED_CLIENT_MONGO_PORT, parser=int),
        )
        return config
