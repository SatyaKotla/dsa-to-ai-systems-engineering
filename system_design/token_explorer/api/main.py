from fastapi import FastAPI
from system_design.token_explorer.services.token_service import TokenService
from system_design.token_explorer.api.models.token_request import TokenRequest
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Token Explorer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/tokenize")
def tokenize(request: TokenRequest):

    token_service = TokenService(num_merges=request.num_merges)

    return token_service.compare(request.text)
