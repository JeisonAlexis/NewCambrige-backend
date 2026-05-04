from pydantic import BaseModel

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre: str
    correo: str

    class Config:
        from_attributes = True