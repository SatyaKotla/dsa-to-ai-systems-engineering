from fastapi import FastAPI
from system_design.token_explorer.services.token_service import TokenService
from system_design.token_explorer.api.models.token_request import TokenRequest

app = FastAPI(title="Token Explorer API")

token_service = TokenService()


@app.post("/tokenize")
def tokenize(request: TokenRequest):

    return token_service.compare(request.text)
