from ml_logic.model import *
from params import *
from utils import image_loader



def generate_detailed_description(language, image_path = IMAGE_PATH):
    image= image_loader(image_path)
    inputs= processor_func(image)
    caption = caption_generator(**inputs)
    detailed_description = image_description(caption, PROMPT, image, language)

    return detailed_description


def text_to_speech(description, image_path, language):
    return speech_maker(description, image_path, language)



if __name__ == '__main__':

    try:
        description = generate_detailed_description(LANGUAGE, IMAGE_PATH)
        print("Generated Description:", description)
        #description = 'hello i am shahab how are you'
        text_to_speech(description, IMAGE_PATH, LANGUAGE)

    except:
        import sys
        import traceback

        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
