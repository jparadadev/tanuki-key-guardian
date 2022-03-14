from abc import ABC, abstractmethod

from fastapi import Request
from fastapi.responses import JSONResponse


class KeyhubController(ABC):

    @abstractmethod
    async def run(self, req: Request) -> JSONResponse:
        raise NotImplementedError()
