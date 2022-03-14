from src.contexts.shared.domain.Interface import Interface


class Decrypter(Interface):

    def decrypt(self, plain_data: str):
        raise NotImplementedError()
