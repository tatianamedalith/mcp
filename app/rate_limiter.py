from fastmcp.server.middleware.rate_limiting import RateLimitingMiddleware

from app.config import Config

rate_limit_middleware = RateLimitingMiddleware(
    max_requests_per_second=Config.RATE_LIMIT_RPS,
    burst_capacity=Config.RATE_LIMIT_BURST,
)
