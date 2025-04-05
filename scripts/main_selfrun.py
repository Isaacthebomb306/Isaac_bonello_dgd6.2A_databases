from fastapi import FastAPI, UploadFile, File
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI()
client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client["game_db"]

@app.get("/")
async def root():#simple test to check if the server is running
    return {"message": "Welcome to the Game API!", "version": "1.0"}

@app.post("/upload/sprite")
async def upload_sprite(file: UploadFile = File(...)):#upload sprite files to the database
    content = await file.read()
    result = await db.sprites.insert_one({"filename": file.filename, "data": content})
    return {"id": str(result.inserted_id)}

@app.post("/upload/audio")
async def upload_audio(file: UploadFile = File(...)):#upload audio files to the database
    content = await file.read()
    result = await db.audio_files.insert_one({"filename": file.filename, "data": content})
    return {"id": str(result.inserted_id)}

@app.post("/submit-score")
async def submit_score(score: dict):#submit score data to the database
    # Validate the score data
    if "player_name" not in score or "score" not in score:
        return {"error": "Invalid data"}
    result = await db.player_scores.insert_one(score)
    return {"id": str(result.inserted_id)}

uvicorn.run(app,host="127.0.0.1", port=8000, log_level="info")
