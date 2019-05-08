import os
import io

from google.cloud import vision
from google.cloud.vision import types

credentials = "/Users/simonpersson/Documents/GitHub/cloud-vision-test/credentials/cloud-vision-test-98fe0bc61133.json"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials

client = vision.ImageAnnotatorClient()

file_name = os.path.join(
    os.path.dirname(__file__), input('Enter file name: '))

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = client.document_text_detection(image=image)

text_annotations = response.text_annotations

for annotation in text_annotations:
    print(annotation.description)
