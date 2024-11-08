import pytesseract
from PIL import Image

# Open an image file
img = Image.open('C:\Python\Data\TestDataImage1.png')

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(img)

print(text)