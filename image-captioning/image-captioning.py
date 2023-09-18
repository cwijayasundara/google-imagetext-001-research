import vertexai

from google.cloud import aiplatform
from vertexai.preview.vision_models import ImageCaptioningModel
from vertexai.preview.vision_models import Image

PROJECT_ID = ""
REGION = "us-central1"

aiplatform.init(
    project=PROJECT_ID,
    location=REGION
)
vertexai.init(
    project=PROJECT_ID,
    location=REGION
)


image_captioning_model = ImageCaptioningModel.from_pretrained("imagetext@001")

# Load the image file as Image object
cloud_next_image = Image.load_from_file("palm2-multimodalembedding"
                                        "/image-captioning/images/img.png")
response = image_captioning_model.get_captions(
    image=cloud_next_image,
    number_of_results=3,
)

print(response)

