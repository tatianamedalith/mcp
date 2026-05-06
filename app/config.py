import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    #JWT
    JWT_SECRET = os.getenv("JWT_SECRET_KEY", "tu_clave_secreta_minimo_32_caracteres")
    JWT_ISSUER = os.getenv("JWT_ISSUER", "lexi-mcp-server")
    JWT_AUDIENCE = os.getenv("JWT_AUDIENCE", "lexi-mcp")
    
    # Servidor
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", "8000"))
    RATE_LIMIT_RPS = float(os.getenv("RATE_LIMIT_RPS", "1.67"))   # 100 req/min
    RATE_LIMIT_BURST = int(os.getenv("RATE_LIMIT_BURST", "20"))
    
    
    EMAIL_PROVIDER = os.getenv("EMAIL_PROVIDER", "smtp")
    
    #SMTP
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_FROM = os.getenv("SMTP_FROM")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    
    #Exchange
    EXCHANGE_USER = os.getenv("EXCHANGE_USER")
    EXCHANGE_PASSWORD = os.getenv("EXCHANGE_PASSWORD")
    EXCHANGE_EMAIL = os.getenv("EXCHANGE_EMAIL")
    
    #TASK
    PYTHON_PATH = os.getenv("PYTHON_PATH", "python")
    
    # Firma del correo
    SIGNATURE_NAME = os.getenv("SIGNATURE_NAME", "Tu Nombre")
    SIGNATURE_ROLE = os.getenv("SIGNATURE_ROLE", "Tu Rol")
    SIGNATURE_LOGO = os.getenv("SIGNATURE_LOGO", "https://res.cloudinary.com/dqgpis4fg/image/upload/v1777557074/skptrceca3cyqlv5xspo.png")
    

    

    