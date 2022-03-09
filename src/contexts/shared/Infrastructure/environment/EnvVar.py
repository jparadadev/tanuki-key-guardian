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

    SHARED_DEVICE_MONGO_HOST = 'shared.device.mongo.host'
    SHARED_DEVICE_MONGO_PORT = 'shared.device.mongo.port'
