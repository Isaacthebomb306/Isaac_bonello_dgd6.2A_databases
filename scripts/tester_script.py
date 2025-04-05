import requests
import random
import string
from fastapi import UploadFile, File

# Base URL of the API
BASE_URL = "http://127.0.0.1:8000/"

# Function to generate a random string of fixed length
def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def upload_sprite(file_path):
    with open(file_path, "rb") as file:
        response = requests.post(f"{BASE_URL}upload/sprite", files={"file": file})
        return response.json()

def upload_audio(file_path):
    with open(file_path, "rb") as file:
        response = requests.post(f"{BASE_URL}upload/audio", files={"file": file})
        return response.json()

def submit_score(player_name, score):
    score_data = {
        "player_name": player_name,
        "score": score
    }
    response = requests.post(f"{BASE_URL}submit-score", json=score_data)
    return response.json()

# Test the upload_sprite function
sprite_response = upload_sprite("path/to/sprite.png")
print("Sprite Upload Response:", sprite_response)

# Test the upload_audio function
audio_response = upload_audio("path/to/audio.mp3")
print("Audio Upload Response:", audio_response)

# Test the submit_score function
player_name = random_string()
score = random.randint(0, 100)
score_response = submit_score(player_name, score)
print("Score Submission Response:", score_response)
