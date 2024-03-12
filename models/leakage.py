from pydantic import BaseModel


class Leakage(BaseModel):
    message: str
    content: str
    pattern: str
