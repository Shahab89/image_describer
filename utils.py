from PIL import Image

def image_loader(image_path):
    return Image.open(image_path).convert('RGB')


def remove_newlines(text):
    return text.replace('\n', '')
