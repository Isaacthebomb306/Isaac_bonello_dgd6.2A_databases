from fastapi import FastAPI, UploadFile, File
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI()
client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client["game_db"]

@app.post("/upload/sprite")
async def upload_sprite(file: UploadFile = File(...)):
    content = await file.read()
    result = await db.sprites.insert_one({"filename": file.filename, "data": content})
    return {"id": str(result.inserted_id)}

@app.post("/upload/audio")
async def upload_audio(file: UploadFile = File(...)):
    content = await file.read()
    result = await db.audio_files.insert_one({"filename": file.filename, "data": content})
    return {"id": str(result.inserted_id)}

@app.post("/submit-score")
async def submit_score(score: dict):
    # Validate the score data
    if "player_name" not in score or "score" not in score:
        return {"error": "Invalid data"}
    result = await db.player_scores.insert_one(score)
    return {"id": str(result.inserted_id)}
