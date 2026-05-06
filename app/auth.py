from fastmcp.server.auth.providers.jwt import JWTVerifier
from app.config import Config

token_verifier = JWTVerifier(
    algorithm="HS256",
    public_key=Config.JWT_SECRET,
    issuer=Config.JWT_ISSUER,
    audience=Config.JWT_AUDIENCE,
)