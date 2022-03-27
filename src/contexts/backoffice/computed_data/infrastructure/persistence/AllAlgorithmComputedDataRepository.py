import sys

from cryptography.hazmat.primitives import hashes, serialization, hmac
from cryptography.hazmat.primitives._serialization import PublicFormat, Encoding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_parameters

from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyTypes
from src.contexts.backoffice.computed_data.domain.entities.ComputedData import ComputedData
from src.contexts.backoffice.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.backoffice.computed_data.domain.entities.ComputedDataOutput import ComputedDataOutput
from src.contexts.backoffice.computed_data.domain.entities.ComputedDataType import ComputedDataType
from src.contexts.backoffice.computed_data.domain.repositories.ComputedDataRepository import ComputedDataRepository
from src.contexts.shared.domain.BaseObject import BaseObject


class AllAlgorithmComputedDataRepository(BaseObject, ComputedDataRepository):

    async def find_one_by_crypto_key_and_input(self, key: CryptoKey, input: ComputedDataInput,
                                               cd_type: ComputedDataType) -> ComputedData:
        output = input.value()
        if key.type.value() == CryptoKeyTypes.DIFFIE_HELLMAN.value:
            output = await self.ecdh_get_shared_key_platform(key.payload.value())

        if key.type.value() == CryptoKeyTypes.DIFFIE_HELLMAN_HMAC.value:
            parameters = key.parameters.value()
            dh_parameters = parameters['parameters']
            signature = parameters['signature']
            output = await self.hmac_DH_GetSharedKey_Platform(dh_parameters, key.payload.value(), signature)

        data = ComputedData(
            input,
            ComputedDataOutput(output),
            key.id,
            cd_type,
        )
        return data

    async def ecdh_get_shared_key_platform(self, public_key_IoT: str):
        # Input para shared key Platform: ID clave pública IoT
        # Returns shared key IoT

        # Plataforma genera su clave pública y privada (y la pública se almacena en la bbdd para el IoT)
        private_key = ec.generate_private_key(ec.SECP384R1())
        public_key = private_key.public_key()
        str_public_key = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo).decode('utf-8')

        # 1. Obtener clave pública en string de la bd y pasar a objeto key
        public_key_IoT_pem = public_key_IoT.encode('utf-8')
        loaded_public_key_IoT = load_pem_public_key(public_key_IoT_pem)

        # Returns shared key platform
        shared_key = private_key.exchange(ec.ECDH(), loaded_public_key_IoT)

        return shared_key.hex()

    async def hmac_DH_GetSharedKey_Platform(self, dh_parameters: str, public_key_IoT: str, pk_signature: str):
        # A la API le llega el id de la clave y de ahí saca el string de parámetros y de la public key del IoT

        # En este punto, el KMS ya tiene los dh_parameters y la clave pública en string y debe convertirlo al objeto original
        # 1. Conversión a bytes y deserialización de parámetros
        dh_parameters_pem = dh_parameters.encode("utf-8")
        loaded_dh_params = load_pem_parameters(dh_parameters_pem)

        # 2. Conversión a bytes y deserialización de clave pública IoT
        public_key_IoT_pem = public_key_IoT.encode('utf-8')
        loaded_public_key_IoT = load_pem_public_key(public_key_IoT_pem)

        # Comprueba que la clave pública del IoT es correcta
        if (not isinstance(loaded_dh_params, dh.DHParameters) or not isinstance(loaded_public_key_IoT, dh.DHPublicKey)):
            sys.exit('Protocol error: Platform received a wrong message!')

        # Comprueba la autenticidad con la HMAC recibida
        h_IoT = hmac.HMAC(public_key_IoT_pem, hashes.SHA256())
        h_IoT.update(b"Platform public key hash")
        h_IoT.verify(bytes.fromhex(pk_signature))

        # 3. Plataforma genera sus propias claves privadas y públicas
        platform_private_key = loaded_dh_params.generate_private_key()
        platform_public_key = platform_private_key.public_key()  # El KMS debe guardar esta clave pública junto con los parámetros y str_signature en la bbdd con id platform-HMACDH
        platform_pk_pem = platform_public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
        str_platform_pk = platform_pk_pem.decode('utf-8')

        # HMAC
        h = hmac.HMAC(platform_pk_pem, hashes.SHA256())
        h.update(b"Platform public key hash")
        signature = h.finalize()
        str_signature = signature.hex()

        shared_key = platform_private_key.exchange(loaded_public_key_IoT)
        # Devuelve la clave en string, el IoT debe enviar al KMS luego de nuevo esta clave para que la almacene
        return shared_key.hex()
