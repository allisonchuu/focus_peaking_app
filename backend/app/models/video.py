from pydantic import BaseModel

class VideoProcessingRequest(BaseModel):
    """Model for optional video processing parameters."""
    threshold1: int = 50
    threshold2: int = 150
    blur_kernel: int = 5

class VideoProcessingResponse(BaseModel):
    """Response model for processed video."""
    message: str
    download_url: str