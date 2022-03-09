from typing import Any

from pydantic import BaseModel, Field


class CreateDeviceCommandDto(BaseModel):

    id: str = Field(example='c5285ee9-1599-46c4-bb9e-1876ef64c72b')
    name: str = Field(example='ESP8266/76125371')
