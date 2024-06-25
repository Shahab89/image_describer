import os

##################  VARIABLES  ##################
MAX_NEW_TOKENS= int(os.environ.get('MAX_NEW_TOKENS'))
PROMPT = "Describe the image in detail for a blind person can sense it:"
IMAGE_PATH = os.environ.get('IMAGE_PATH')

BLIP_PROCESSOR = os.environ.get('BLIPPROCESSOR')
Blip_For_Conditional_Generation = os.environ.get('BlipForConditionalGeneration')
MODE = os.environ.get('MODE')
MODEL_NAME = os.environ.get('MODEL_NAME')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
SOUNDS_OUTPUT_DIR = os.environ.get('SOUNDS_OUTPUT_DIR')





HG_EMBEDDING_MODEL = os.environ.get('HG_EMBEDDING_MODEL')


MODE_STEP_1 = os.environ.get('MODE_STEP_1')
MODEL_NAME_STEP_1 = os.environ.get('MODEL_NAME_STEP_1')

MODE_STEP_2 = os.environ.get('MODE_STEP_2')
MODEL_NAME_STEP_2 = os.environ.get('MODEL_NAME_STEP_2')




LANGUAGE = os.environ.get('LANGUAGE')
##################  CONSTANTS  ##################
MODEL_DIR = "models"
CHROMA_PERSIST_DIR = os.path.join('db', 'chroma_3')

LANGUAGE_DICT = {'German':'de',
                 'English': 'en'
                 }
