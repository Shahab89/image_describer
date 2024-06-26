import json
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

from fastapi.middleware.cors import CORSMiddleware
from transformers import BlipProcessor, BlipForConditionalGeneration
from params import *
from openai import OpenAI
from utils import image_loader
from ml_logic.model import *
from interface.main import *
import os
import aiofiles

from fastapi import Query, HTTPException

# Preload models for computing speed

processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')


app = FastAPI()
app.state.model = model

# Global variable to store the last uploaded image path
last_uploaded_image = None
description = None

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)




@app.post("/upload_image")
async def upload_image(image: UploadFile = File(...)) -> str:
    global last_uploaded_image
    # You can save the uploaded file or process it here
    image_location = os.path.join(IMAGE_PATH, image.filename)
    # Save the uploaded file asynchronously
    async with aiofiles.open(image_location, "wb") as file:
        content = await image.read()
        await file.write(content)
    last_uploaded_image = image_location
    return  image_location






@app.get('/description')
def generate_description(language) -> str:
    global last_uploaded_image
    global description
    description= generate_detailed_description(language, last_uploaded_image)
    return description

# @app.get("/speech")
# def audio_maker(language):
#     text_to_speech(description, last_uploaded_image, language)
#     return 'audio succesfully saved!'



@app.get("/speech")
def audio_maker(language: str):
    global last_uploaded_image
    global description
    audio_path = text_to_speech(description, last_uploaded_image, language)
    image_name = os.path.basename(last_uploaded_image).split('.')[0]
    return FileResponse(audio_path, media_type='audio/mpeg', filename=f'audio_{image_name}_{LANGUAGE_DICT[language]}.mp3')




# @app.get("/speech")
# def audio_maker(language: str) -> FileResponse:
#     if language not in LANGUAGE_DICT:
#         raise HTTPException(status_code=400, detail="Invalid language parameter.")

#     if not description or not last_uploaded_image:
#         raise HTTPException(status_code=404, detail="Description or image path not available.")

#     audio_path = text_to_speech(description, last_uploaded_image, language)
#     if audio_path is None:
#         raise HTTPException(status_code=500, detail="Failed to generate audio file.")

#     image_name = os.path.basename(last_uploaded_image).split('.')[0]
#     print('audio_path:', audio_path)
#     print ('filename:  ', f'audio_{image_name}_{LANGUAGE_DICT[language]}.mp3')
#     return FileResponse(audio_path, media_type='audio/mpeg', filename=f'audio_{image_name}_{LANGUAGE_DICT[language]}.mp3')





@app.get("/")
def root() -> str:
    return "Intelligent Image describer API. See endpoint /docs for documentation."
