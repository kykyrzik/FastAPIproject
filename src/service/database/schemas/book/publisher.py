from pydantic import BaseModel


class PublisherDTO(BaseModel):
    id: int
    publisher_name: str

    class Config:
        orm_mode = True
