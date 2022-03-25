from typing import Tuple

from cryptography.hazmat.backends.openssl import ec, dh

from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyTypes


async def generate_key(self, crypto_key_type: str) -> Tuple[str, str]:
    private_key = None
    if crypto_key_type == CryptoKeyTypes.DIFFIE_HELLMAN_ELLIPTIC_CURVE:
        private_key = ec.generate_private_key(ec.SECP384R1())

    if crypto_key_type == CryptoKeyTypes.DIFFIE_HELLMAN_HMAC:
        parameters = dh.generate_parameters(generator=2, key_size=512)
        private_key = parameters.generate_private_key()

    if private_key is None:
        raise Exception('Algorithm not suported')

    public_key = self.private_key.public_key()
    return private_key, public_key
