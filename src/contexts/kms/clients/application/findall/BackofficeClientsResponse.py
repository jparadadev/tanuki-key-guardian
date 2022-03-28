from typing import List, Any

from src.contexts.kms.clients.domain.entities.Client import Client
from src.contexts.shared.domain.Metadata import Metadata
from src.contexts.shared.domain.Response import Response


class BackofficeClientsResponse(Response):

    def __init__(
            self,
            clients: List[Client],
            metadata: Metadata = None,
    ):
        self._clients = clients
        self._meta = metadata

    def to_primitives(self) -> Any:
        json_clients = [client.to_primitives() for client in self._clients]
        response = {
            'data': json_clients,
        }
        if self._meta is not None:
            response['metadata'] = self._meta.to_dict()
        return response
