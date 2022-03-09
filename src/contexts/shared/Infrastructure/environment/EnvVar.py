from enum import Enum


class EnvVar(Enum):

    ENV_MODE = 'env_mode'

    # -------------------------------------------------------
    # -------------------- BACKOFFICE -----------------------
    # -------------------------------------------------------

    BACKOFFICE_SERVER_HOST = 'backoffice.server.host'
    BACKOFFICE_SERVER_PORT = 'backoffice.server.port'

    # -------------------------------------------------------
    # ---------------------- SHARED -------------------------
    # -------------------------------------------------------

    SHARED_CLIENT_MONGO_HOST = 'shared.client.mongo.host'
    SHARED_CLIENT_MONGO_PORT = 'shared.client.mongo.port'
