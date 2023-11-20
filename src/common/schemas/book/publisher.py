from pydantic import BaseModel


class PublisherDTO(BaseModel):
    id: int
    publisher_name: str

    class Config:
        from_attributes = True
