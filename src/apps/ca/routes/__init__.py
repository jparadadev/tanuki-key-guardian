from fastapi import APIRouter

from src.apps.ca.routes.status_routes import register as register_status_routes
from src.apps.ca.routes.cryptokey_routes import register as register_cryptokey_routes


def register_routes(router: APIRouter):
    register_status_routes(router)
    register_cryptokey_routes(router)
