from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import memory

app = FastAPI()

# CORS so frontend can access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route modules
app.include_router(memory.router, prefix="/memory", tags=["Memory"])
