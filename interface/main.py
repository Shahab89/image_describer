from ml_logic.model import *
from params import *
from utils import image_loader



def generate_detailed_description():
    image= image_loader(IMAGE_PATH)
    inputs= processor_func(image)
    caption = caption_generator(**inputs)
    detailed_description = image_description(caption, PROMPT, image)

    return detailed_description


def text_to_speech(description):
    speech_maker(description)



if __name__ == '__main__':

    try:
        description = generate_detailed_description()
        print("Generated Description:", description)
        #description = 'hello i am shahab how are you'
        text_to_speech(description)

    except:
        import sys
        import traceback

        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
