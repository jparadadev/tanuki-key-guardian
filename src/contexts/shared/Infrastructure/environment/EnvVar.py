from enum import Enum


class EnvVar(Enum):

    ENV_MODE = 'env_mode'

    # -------------------------------------------------------
    # -------------------- BACKOFFICE -----------------------
    # -------------------------------------------------------

    BACKOFFICE_SERVER_HOST = 'kms.server.host'
    BACKOFFICE_SERVER_PORT = 'kms.server.port'

    # -------------------------------------------------------
    # -------------------- CA -----------------------
    # -------------------------------------------------------

    CA_SERVER_HOST = 'ca.server.host'
    CA_SERVER_PORT = 'ca.server.port'

    # -------------------------------------------------------
    # ---------------------- SHARED -------------------------
    # -------------------------------------------------------

    SHARED_CLIENT_MONGO_HOST = 'shared.client.mongo.host'
    SHARED_CLIENT_MONGO_PORT = 'shared.client.mongo.port'

    SHARED_CRYPTOKEY_MONGO_HOST = 'shared.cryptokey.mongo.host'
    SHARED_CRYPTOKEY_MONGO_PORT = 'shared.cryptokey.mongo.port'
