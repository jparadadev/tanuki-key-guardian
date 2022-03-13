from pydantic import BaseModel, Field


class CreateCryptoKeyCommandDto(BaseModel):

    id: str = Field(example='c5285ee9-1599-46c4-bb9e-1876ef64c72b')
    client: str = Field(example='c2285aa9-1599-36c3-bb9e-1876ef64372b', alias='client-id')
    type: str = Field(example='rsa')
    payload: str = Field(example='AAAAB3NzaC1yc2EAAAADAQABAAABgQDoEoDbPH/wE7fmSySqSndZtJwh5Pc7Q5L5I/DPVnUtgu02QwhzwEsdmR4Z1tKPst2OMCc/Gn6UQdKAmVUxXOWknIqQxuzmJwO4kCNPjNrrdmM4uLkIQxkJnk2vmMVM3LubCfWVIqmNBzl3fPN5qxl2kZlo1rkd1zx2gIND8CMRK7wNLmogchk4EudU5INGbexE/eSGJiFRQyShRN9tNewR80S0hA02Ku3wk8bYA+rLcupLH39LgmrH5KIYp3YDB0svUFv6ieBTdfk04+8X0u0DmFhq+6L5xND9HIxwyeU4LTA7vFWevB3rFq7p9kCsWd1Zv/LFjZDkdL6SsUuOgVGTaWBuP1BUDtI2/+U+/O3kiOE9+/W3tRm8Dc91DkT43F7jmevAepdsZYTnqHYAZ47NRGOAyE38J5wWR8HFhWQ+EMffdxdgMPdl1prkI0GAB3CdqwG/i99cZs7vQV8MHqumVivHQnvwv1paZv0cVihAEFgFDyDrbpwcqcPsvynb0h8')
