from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives._serialization import PublicFormat, Encoding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import load_pem_public_key


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
        output = ''
        if key.type.value() == CryptoKeyTypes.DIFFIE_HELLMAN.value:
            output = await self.ecdh_get_shared_key_platform(key.payload.value())

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
