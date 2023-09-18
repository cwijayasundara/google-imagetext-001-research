from pytesseract import image_to_string
from PIL import Image

image = Image.open('/palm2-multimodalembedding/text-extraction-from'
                   '-image/images/zoumana_article_information.png', mode='r')

print(image_to_string(image))

image = Image.open('/palm2-multimodalembedding/text-extraction-from'
                   '-image/images/img.png', mode='r')
print(image_to_string(image))