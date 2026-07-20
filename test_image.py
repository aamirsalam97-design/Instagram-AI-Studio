from PIL import Image
from utils.gemini_api import generate_caption

img = Image.open("test.jpg")   # apni koi jpg image ka naam

print(generate_caption(img, "Professional"))