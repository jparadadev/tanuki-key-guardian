from src.contexts.shared.domain.Interface import Interface


class Encrypter(Interface):

    def encrypt(self, plain_data: str):
        raise NotImplementedError()
