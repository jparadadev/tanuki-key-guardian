from fastapi import APIRouter

from src.apps.backoffice.backend.routes.status_routes import register as register_status_routes
from src.apps.backoffice.backend.routes.client_routes import register as register_client_routes
from src.apps.backoffice.backend.routes.cryptokey_routes import register as register_cryptokey_routes
from src.apps.backoffice.backend.routes.computed_data_routes import register as register_computed_data_routes
from src.apps.kms.routes.key_routes import register as register_key_routes


def register_routes(router: APIRouter):
    register_status_routes(router)
    register_client_routes(router)
    register_cryptokey_routes(router)
    register_computed_data_routes(router)
    register_key_routes(router)
