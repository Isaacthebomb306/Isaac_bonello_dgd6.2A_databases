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
    result = await db.player_scores.insert_one(score)
    return {"id": str(result.inserted_id)}

uvicorn.run(app,host="127.0.0.1", port=8000, log_level="info")