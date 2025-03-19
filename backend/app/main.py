from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(video.router)

@app.get("/")
def home():
    return {"message": "Focus-peaking video processing running."}

