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
    '''Generate a random string of fixed length | 
    length can't be negative or zero | 
    length can't be greater than 25'''
    if length < 0:
        length = length * -1
    if length == 0:
        length = 10
    if length > 25:
        length = 25
    
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

# Test the submit_score function with a random player name and score, 20 times
for _ in range(20):
    score = random.randint(-5, 100)
    player_name = random_string(score)
    score_response = submit_score(player_name, score)
    print("Score Submission Response:", score_response)

'''
# Test the submit_score function with invalid data
invalid_score_response = submit_score("", "")
print("Invalid Score Submission Response:", invalid_score_response)
# Test the submit_score function with invalid score type
invalid_score_response = submit_score("Player1", "InvalidScore")
print("Invalid Score Submission Response:", invalid_score_response)
# Test the submit_score function with negative score
invalid_score_response = submit_score("Player1", -10)
print("Invalid Score Submission Response:", invalid_score_response)
# Test the submit_score function with empty player name
invalid_score_response = submit_score("", 50)
print("Invalid Score Submission Response:", invalid_score_response)
# Test the submit_score function with empty score
invalid_score_response = submit_score("Player1", "")
print("Invalid Score Submission Response:", invalid_score_response)
# Test the submit_score function with non-string player name
invalid_score_response = submit_score(123, 50)
print("Invalid Score Submission Response:", invalid_score_response)
'''
