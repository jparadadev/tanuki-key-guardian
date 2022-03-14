from abc import abstractmethod

from src.contexts.shared.domain.Interface import Interface


class Decrypter(Interface):

    @abstractmethod
    def decrypt(self, plain_data: str, key: str):
        raise NotImplementedError()
