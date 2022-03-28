import sys

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives._serialization import PublicFormat, Encoding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_parameters

from src.contexts.kms.computed_data.domain.entities.ComputedDataMeta import ComputedDataMeta
from src.contexts.kms.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.kms.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyTypes
from src.contexts.kms.computed_data.domain.entities.ComputedData import ComputedData
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.kms.computed_data.domain.entities.ComputedDataOutput import ComputedDataOutput
from src.contexts.kms.computed_data.domain.entities.ComputedDataType import ComputedDataType, ComputedDataTypes
from src.contexts.kms.computed_data.domain.repositories.ComputedDataRepository import ComputedDataRepository
from src.contexts.shared.domain.BaseObject import BaseObject


class AllAlgorithmComputedDataRepository(BaseObject, ComputedDataRepository):

    async def find_one_by_crypto_key_and_input(self, key: CryptoKey, input: ComputedDataInput,
                                               cd_type: ComputedDataType) -> ComputedData:
        output = input.value()
        meta = {}
        if key.type.value() == CryptoKeyTypes.DIFFIE_HELLMAN.value:
            output, meta = await self.ecdh_get_shared_key_platform(key.payload.value())

        if key.type.value() == CryptoKeyTypes.DIFFIE_HELLMAN_HMAC.value:
            parameters = key.parameters.value()
            dh_parameters = parameters['parameters']
            signature = parameters['signature']
            output, meta = await self.hmac_DH_GetSharedKey_Platform(dh_parameters, key.payload.value(), signature)

        if key.type.value() == CryptoKeyTypes.AE.value and cd_type.value() == ComputedDataTypes.ENCRYPT.value:
            output, meta = await self.encryption_AE(key.payload.value(), input.value())

        if key.type.value() == CryptoKeyTypes.AE.value and cd_type.value() == ComputedDataTypes.DECRYPT.value:
            text, nonce = tuple(input.value().split('@'))
            output, meta = await self.decrypt_AE(key.payload.value(), text, nonce)

        if key.type.value() == CryptoKeyTypes.AEAD.value and cd_type.value() == ComputedDataTypes.ENCRYPT.value:
            output, meta = await self.Encryption_AEAD(key.payload.value(), input.value())

        if key.type.value() == CryptoKeyTypes.AEAD.value and cd_type.value() == ComputedDataTypes.DECRYPT.value:
            text, nonce = tuple(input.value().split('@'))
            output, meta = await self.Decrypt_AEAD(text, key.payload.value(), nonce)

        data = ComputedData(
            input,
            ComputedDataOutput(output),
            key.id,
            cd_type,
            ComputedDataMeta(meta),
        )
        return data

    async def Encryption_AEAD(self, passphrase: str, sensitive_data: str):
        # Key generation
        key_gen = b"/\x84F\xc5\xddA^k\xd2.C\x19'\x1a2\x9c"  # Key derivation
        key = PBKDF2(passphrase, key_gen)  # Contraseña basada en key derivation
        print("AES Encryption Key: " + str(key))

        # Data sensitiva para cifrar
        print("Data enviada para cifrar: " + "\n" + str(sensitive_data))

        # Encriptación usando AES GCM
        cipher = AES.new(key, AES.MODE_GCM)  # https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
        ciphertext = cipher.encrypt(sensitive_data.encode('utf-8'))
        nonce = cipher.nonce

        # Mensaje transmitido
        # ciphertext: resultado de los datos cifrados,
        # tag: Codigo de autenticacion de mensajes MAC
        # nonce: vector de inicializacion (solo ocurre una vez)

        transmitted_message = ciphertext.hex()
        print("\nMensaje transmitido: " + str(transmitted_message))
        return f'{transmitted_message}@{nonce.hex()}', {'nonce': nonce.hex()}

    async def Decrypt_AEAD(self, transmitted_message: str, passphrase: str, nonce: str) -> str:
        received_kdf_salt = b"/\x84F\xc5\xddA^k\xd2.C\x19'\x1a2\x9c"
        received_msg = transmitted_message
        print("Mensaje recibido: " + str(received_msg))
        received_ciphertext = received_msg
        # Generate decryption key from passphrase and salt
        decryption_key = PBKDF2(passphrase, received_kdf_salt)
        print("Decryption Key: " + str(decryption_key))
        cipher = AES.new(decryption_key, AES.MODE_GCM, bytes.fromhex(nonce))
        try:
            decrypted_data = cipher.decrypt(bytes.fromhex(received_ciphertext))
            print("\nMAC validated: Data was encrypted by someone with the shared secret passphrase")
            print("All allies have passphrase - SYMMETRIC encryption!!!")
            print("Data descifrada: " + str(decrypted_data))
        except Exception as e:
            print("\nFallo de la validación MAC durante la desencriptación. Auntenticación no garantizada")

        return (decrypted_data).decode(), {}

    async def encryption_AE(self, passphrase: str, sensitive_data: str):
        # Key generation
        key_gen = b"/\x84F\xc5\xddA^k\xd2.C\x19'\x1a2\x9c"  # Key derivation
        key = PBKDF2(passphrase, key_gen)  # Contraseña basada en key derivation
        print("AES Encryption Key: " + str(key))

        # Data sensitiva para cifrar
        print("Data enviada para cifrar: " + "\n" + str(sensitive_data))

        # Encriptación usando AES GCM
        cipher = AES.new(key, AES.MODE_GCM)  # https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
        ciphertext, tag = cipher.encrypt_and_digest(sensitive_data.encode('utf-8'))
        nonce = cipher.nonce

        # Mensaje transmitido
        # ciphertext: resultado de los datos cifrados,
        # tag: Codigo de autenticacion de mensajes MAC
        # nonce: vector de inicializacion (solo ocurre una vez)
        transmitted_message = ciphertext.hex()
        meta = {
            'tag': tag.hex(),
            'nonce': nonce.hex(),
        }
        print("\nMensaje transmitido: " + str(transmitted_message))
        print(type(transmitted_message))
        return f'{transmitted_message}@{nonce.hex()}', meta

    async def decrypt_AE(self, passphrase: str, transmitted_message: str, nonce: str):
        received_msg = transmitted_message
        print("\nMensaje recibido: " + str(received_msg))
        received_kdf_salt = b"/\x84F\xc5\xddA^k\xd2.C\x19'\x1a2\x9c"  # Key derivation
        received_ciphertext, received_nonce = bytes.fromhex(transmitted_message), bytes.fromhex(nonce)

        # Generar decryption key con la contraseña y salt
        decryption_key = PBKDF2(passphrase, received_kdf_salt)
        print("Decryption Key: " + str(decryption_key))

        # Validar MAC y descifrar, si la validación MAC falla, ValueError exception se va a mostrar
        cipher = AES.new(decryption_key, AES.MODE_GCM, received_nonce)
        try:
            decrypted_data = cipher.decrypt(received_ciphertext)
            print("Data descifrada: " + str(decrypted_data))
        except ValueError as mac_mismatch:
            print("\nFallo de la validación MAC durante la desencriptación. Auntenticación no garantizada")

        return decrypted_data.decode('utf-8'), {}

    async def ecdh_get_shared_key_platform(self, public_key_IoT: str) -> (str, dict):
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

        return shared_key.hex(), {'generated-public-key': str_public_key}

    async def hmac_DH_GetSharedKey_Platform(self, dh_parameters: str, public_key_IoT: str, pk_signature: str) -> (str, dict):
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
        return shared_key.hex(), {'generated-public-key': str_platform_pk, 'signature': str_signature, 'parameters': dh_parameters}
