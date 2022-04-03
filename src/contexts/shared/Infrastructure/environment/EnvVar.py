from enum import Enum


class EnvVar(Enum):
    ENV_MODE = 'env_mode'

    # -------------------------------------------------------
    # ----------------------- KMS ---------------------------
    # -------------------------------------------------------

    KMS_SERVER_HOST = 'kms.server.host'
    KMS_SERVER_PORT = 'kms.server.port'

    KMS_CLIENT_MONGO_HOST = 'kms.client.mongo.host'
    KMS_CLIENT_MONGO_PORT = 'kms.client.mongo.port'

    KMS_CRYPTOKEY_MONGO_HOST = 'kms.cryptokey.mongo.host'
    KMS_CRYPTOKEY_MONGO_PORT = 'kms.cryptokey.mongo.port'

    # -------------------------------------------------------
    # ---------------------- SHARED -------------------------
    # -------------------------------------------------------
