from datetime import timedelta


JWT_SECRET_KEY = "secret_key"
JWT_EXPIRES = timedelta(hours=24)
JWT_IDENTITY_CLAIM = "user"
JWT_HEADER_NAME = "authorization"
