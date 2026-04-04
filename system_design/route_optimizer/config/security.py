import os

API_KEY = os.getenv("API_KEY", "dev-secret-key")

# jwt config
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-jwt-secret-key")
