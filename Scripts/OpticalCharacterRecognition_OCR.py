import pytesseract
from PIL import Image

# Open the image file
image = Image.open('C:\Python\Data\TestDataImage1.png')

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
