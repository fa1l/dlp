from pydantic import BaseModel


class Leakage(BaseModel):
    matched_pattern: str
    original_message: str
    pattern: str
