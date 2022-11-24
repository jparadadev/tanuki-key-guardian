from enum import Enum


class EnvVar(Enum):
    ENV_MODE = 'env_mode'

    # -------------------------------------------------------
    # ----------------------- KMS ---------------------------
    # -------------------------------------------------------

    KMS_SERVER_HOST = 'kms_server_host'
    KMS_SERVER_PORT = 'kms_server_port'

    KMS_CLIENT_MONGO_HOST = 'kms_client_mongo_host'
    KMS_CLIENT_MONGO_PORT = 'kms_client_mongo_port'

    # -------------------------------------------------------
    # ---------------------- SHARED -------------------------
    # -------------------------------------------------------
