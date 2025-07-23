from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from main import FindLaneLines

app = FastAPI()
findLaneLines = FindLaneLines()

# ✅ Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Route for image processing
@app.post("/process/")
async def process_image(file: UploadFile = File(...)):
    input_path = "static/input.jpg"
    output_path = "static/output.jpg"

    # Save uploaded file
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run lane + object detection
    findLaneLines.process_image(input_path, output_path)

    return {"message": "Image processed", "output": output_path}

# ✅ Route for video processing
@app.post("/process-video/")
async def process_video(file: UploadFile = File(...)):
    input_path = "static/input.mp4"
    output_path = "static/output.mp4"

    # Save uploaded video
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run video processing
    findLaneLines.process_video(input_path, output_path)

    return {"message": "Video processed", "output": output_path}
