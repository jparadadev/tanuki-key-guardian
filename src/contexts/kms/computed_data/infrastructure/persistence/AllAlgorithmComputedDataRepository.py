from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF



from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.backoffice.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyTypes
from src.contexts.kms.computed_data.domain.entities.ComputedData import ComputedData
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.kms.computed_data.domain.entities.ComputedDataOutput import ComputedDataOutput
from src.contexts.kms.computed_data.domain.entities.ComputedDataType import ComputedDataType
from src.contexts.kms.computed_data.domain.repositories.ComputedDataRepository import ComputedDataRepository
from src.contexts.shared.domain.BaseObject import BaseObject


class AllAlgorithmComputedDataRepository(BaseObject, ComputedDataRepository):

    async def find_one_by_crypto_key_and_input(self, key: CryptoKey, input: ComputedDataInput,
                                               cd_type: ComputedDataType) -> ComputedData:
        output = ''
        if key.type.value() == CryptoKeyTypes.DIFFIE_HELLMAN.value:
            self.__ECDH(key.payload.value(), input.value())

        data = ComputedData(
            input,
            ComputedDataOutput(output),
            key.id,
            cd_type,
        )
        return data



    def __ECDH(self, private_key:str, public_key:str):
        public_key = str.encode(public_key)
        private_key = str.encode(private_key)
        str.de
        # ec.generate_private_key(ec.SECP384R1(), )
        serialization.load_pem_parameters()
        # Input para shared key IoT: ID clave privada IoT, ID clave pública plataforma
        # Returns shared key IoT
        # Input para shared key plataforma: ID clave privada platform, ID clave pública IoT
        # Returns shared key platform
        shared_key = private_key.exchange(ec.ECDH(), public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
        ).derive(shared_key)
        return derived_key
