from abc import abstractmethod

from src.contexts.shared.domain.Interface import Interface


class Encrypter(Interface):

    @abstractmethod
    def encrypt(self, plain_data: str, key: str):
        raise NotImplementedError()
