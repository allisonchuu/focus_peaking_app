from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from app.services.video_processor import process_video
from app.models.video import VideoProcessingRequest, VideoProcessingResponse

router = APIRouter()

UPLOADS_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOADS_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@router.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    uploaded_video_path = f"{UPLOADS_FOLDER}/{file.filename}"
    processed_video_path = f"{PROCESSED_FOLDER}/processed_{file.filename}"

    with open(uploaded_video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        process_video(uploaded_video_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"message":"Processing complete", "download_url":f"/download/{file.filename}"}
        
@router.get("/download/{filename}")
async def download_video(filename: str):
    processed_path = f"{PROCESSED_FOLDER}/processed_{filename}"
    return {"video_path": processed_path}