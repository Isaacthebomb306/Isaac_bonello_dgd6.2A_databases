import requests
import random
import string
import json
import os
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

# Test the upload_sprite function by uploading all the data in data/images
data_dir = "data/images"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
else:
    for filename in os.listdir(data_dir):
        file_path = os.path.join(data_dir, filename)
        if os.path.isfile(file_path):
            sprite_response = upload_sprite(file_path)
            print(f"Sprite Upload Response for {filename}:", sprite_response)

# Test the upload_audio function by uploading all the data in data/audio
data_dir = "data/audio"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
else:
    for filename in os.listdir(data_dir):
        file_path = os.path.join(data_dir, filename)
        if os.path.isfile(file_path):
            audio_response = upload_audio(file_path)
            print(f"Audio Upload Response for {filename}:", audio_response)

# Test the submit_score function
player_name = random_string()
score = random.randint(0, 100)
score_response = submit_score(player_name, score)
print("Score Submission Response:", score_response)
