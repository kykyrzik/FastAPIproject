from pydantic import BaseModel, ConfigDict


class AuthorsDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    surname: str

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"


class AuthorInDB(AuthorsDTO):
    id: int
