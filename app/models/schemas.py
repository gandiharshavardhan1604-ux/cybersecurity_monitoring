from pydantic import BaseModel


class SecurityEvent(BaseModel):
    event_type: str
    username: str
    ip_address: str
    message: str