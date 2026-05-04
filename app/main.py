from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.modules.auth.router import router as auth_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Hola mundo con FastAPI 🚀"}

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # puerto por defecto de Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)