from utils import *

from transformers import BlipProcessor, BlipForConditionalGeneration
from params import *
from openai import OpenAI

from gtts import gTTS
import pygame
import os

processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')

def processor_func (image):
    """
    Prepare the image
    input:
    - image
    return: inputs: outputs the processed tensors
    """
    inputs = processor( image, return_tensors = 'pt')
    return inputs

def caption_generator(**inputs):
    '''
    generate caption for input image
    '''
    out =  model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def image_description(caption, prompt, image, language = LANGUAGE):
    '''
    Generate a detailed description using the caption as context
    '''
    descr_prompt = prompt + caption + f' It must be in {language} language'
    if MODE=='openai':
        client= OpenAI(api_key = OPENAI_API_KEY)
        response = client.chat.completions.create(
        model=MODEL_NAME,  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are an expert at describing images in detail."},
            {"role": "user", "content": descr_prompt}
        ]
        )

        detailed_description = response.choices[0].message.content.strip().strip()
    else:

        inputs = processor(text=descr_prompt, images=image, return_tensors="pt")
        out = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS)  # Set max_new_tokens to handle longer output
        detailed_description = processor.decode(out[0], skip_special_tokens=True)

    return detailed_description


def speech_maker(description, image_path, language = LANGUAGE):
    try:
        tts = gTTS(description, lang=LANGUAGE_DICT[language])
        image_name = os.path.basename(image_path)
        output_dir = os.path.join(SOUNDS_OUTPUT_DIR, f'audio_{image_name}_{LANGUAGE_DICT[language]}.mp3' )
        tts.save(output_dir)
        # client = OpenAI()
        # response = client.audio.speech.create(
        #     model="tts-1",
        #     voice="alloy",
        #     input=description
        # )
        # pygame.mixer.init()
        # pygame.mixer.music.load(SOUNDS_OUTPUT_DIR)
        # pygame.mixer.music.play()

        # # Wait for the audio to finish playing
        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(10)  # Adjust as needed for playback precision


    except Exception as e:
        print(f"An error occurred: {e}")
