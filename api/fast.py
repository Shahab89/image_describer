import json
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from transformers import BlipProcessor, BlipForConditionalGeneration
from params import *
from openai import OpenAI
from utils import image_loader
from ml_logic.model import *
from interface.main import *
import os
import aiofiles


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

    global description
    description= generate_detailed_description(language, last_uploaded_image)
    return description

@app.get("/speech")
def audio_maker(language):
    text_to_speech(description, last_uploaded_image, language)
    return 'audio succesfully saved!'



@app.get("/")
def root() -> str:
    return "Intelligent Image describer API. See endpoint /docs for documentation."
