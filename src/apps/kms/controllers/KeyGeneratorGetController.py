from typing import Tuple

from cryptography.hazmat.backends.openssl.ec import ec
from cryptography.hazmat.backends.openssl.dh import dh
from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.kms.controllers.KmsController import KmsController
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyTypes


class KeyGeneratorGetController(KmsController):

    def __init__(self):
        pass

    async def run(self, req: Request) -> JSONResponse:
        query_params = dict(req.query_params)
        priv, pub = generate_key(query_params.get('algorithm'))
        return JSONResponse(status_code=HTTPStatus.OK, content=JSONResponse({
            'private-key': priv,
            'public-key': pub,
        }))


def generate_key(crypto_key_type: str) -> Tuple[str, str]:
    private_key = None
    if crypto_key_type == CryptoKeyTypes.DIFFIE_HELLMAN_ELLIPTIC_CURVE.value:
        private_key = ec.generate_private_key(ec.SECP384R1())

    if crypto_key_type == CryptoKeyTypes.DIFFIE_HELLMAN_HMAC.value:
        parameters = dh.generate_parameters(generator=2, key_size=512)
        private_key = parameters.generate_private_key()

    if private_key is None:
        raise Exception('Algorithm not suported')

    public_key = private_key.public_key()
    return private_key, public_key

