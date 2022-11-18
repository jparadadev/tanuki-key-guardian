import os

from Crypto.Cipher import AES

from src.contexts.kms.computed_data.domain.entities.ComputedData import ComputedData
from src.contexts.kms.computed_data.domain.entities.ComputedDataInput import ComputedDataInput
from src.contexts.kms.computed_data.domain.entities.ComputedDataMeta import ComputedDataMeta
from src.contexts.kms.computed_data.domain.entities.ComputedDataOutput import ComputedDataOutput
from src.contexts.kms.computed_data.domain.entities.ComputedDataType import ComputedDataType, ComputedDataTypes
from src.contexts.kms.computed_data.domain.repositories.ComputedDataRepository import ComputedDataRepository
from src.contexts.kms.cryptokeys.domain.entities.CryptoKey import CryptoKey
from src.contexts.kms.cryptokeys.domain.entities.CryptoKeyType import CryptoKeyTypes
from src.contexts.shared.domain.BaseObject import BaseObject


async def encrypt_aes(key: CryptoKey, input_data: ComputedDataInput, meta: ComputedDataMeta) -> ComputedData:
    encode = meta.value().get('encode', 'utf-8')

    raw_input: str = input_data.value()
    raw_iv: str = meta.value().get('iv')

    encoded_raw_input = raw_input.encode(encode)

    if raw_iv is not None:
        encoded_raw_iv = raw_iv.encode(encode)
    else:
        encoded_raw_iv = os.urandom(16)

    encoded_key = key.payload.value().encode()

    cipher = AES.new(encoded_key, AES.MODE_EAX, encoded_raw_iv)
    nonce = cipher.nonce

    raw_output, tag = cipher.encrypt_and_digest(encoded_raw_input)
    encoded_output = raw_output.hex()

    output = ComputedDataOutput(encoded_output)
    data_type = ComputedDataType(ComputedDataTypes.ENCRYPT.value)
    data = ComputedData(input_data, output, key.id, data_type, meta)
    return data


async def decrypt_aes(key: CryptoKey, input_data: ComputedDataInput, meta: ComputedDataMeta) -> ComputedData:
    output = ComputedDataOutput(input_data.value())
    data_type = ComputedDataType(ComputedDataTypes.DECRYPT.value)
    data = ComputedData(input_data, output, key.id, data_type, meta)
    return data


class PyCryptodomeComputedDataRepository(BaseObject, ComputedDataRepository):
    _FMAPPING = {
        CryptoKeyTypes.AES.value: {
            ComputedDataTypes.ENCRYPT.value: encrypt_aes,
            ComputedDataTypes.DECRYPT.value: decrypt_aes,
        },
    }

    async def find_one_by_crypto_key_and_input(
            self,
            key: CryptoKey,
            input_data: ComputedDataInput,
            operation_type: ComputedDataType,
            meta: ComputedDataMeta,
    ) -> ComputedData:
        if key.type.value() not in PyCryptodomeComputedDataRepository._FMAPPING:
            raise Exception('Algorithm not found.')

        if operation_type.value() not in PyCryptodomeComputedDataRepository._FMAPPING[key.type.value()]:
            raise Exception('Operation type not found.')

        crypt_func = PyCryptodomeComputedDataRepository._FMAPPING[key.type.value()][operation_type.value()]
        return await crypt_func(key, input_data, meta)
