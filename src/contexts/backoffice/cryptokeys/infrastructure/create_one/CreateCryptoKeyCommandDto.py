from pydantic import BaseModel, Field


class CreateCryptoKeyCommandDto(BaseModel):

    id: str = Field(example='c5285ee9-1599-46c4-bb9e-1876ef64c72b')
    client: str = Field(example='c2285aa9-1599-36c3-bb9e-1876ef64372b', alias='client-id')
    type: str = Field(example='rsa')
    payload: str = Field(example='')
