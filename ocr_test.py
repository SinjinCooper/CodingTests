import pytesseract as tess
pytesseract.pytesseract.tesseract_cmd = r'/anaconda3/lib/python3.6/site-packages/pytesseract/pytesseract.py'
from PIL import Image

img = Image.open('screenShot.png')
text = tess.image_to_string(img)

print(img)