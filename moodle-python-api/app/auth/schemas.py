from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int  # seconds


class LoginRequest(BaseModel):
    username: str
    password: str
    service: str = "moodle_mobile_app"  # matches Moodle token service names
