from pydantic import BaseModel


class TokenRequest(BaseModel):

    text: str
    num_merges: int = 1
