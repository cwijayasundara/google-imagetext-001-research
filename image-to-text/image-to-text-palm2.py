import vertexai

from google.cloud import aiplatform
from vertexai.preview.vision_models import ImageQnAModel
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

image_qna_model = ImageQnAModel.from_pretrained("imagetext@001")

# Load the image file as Image object
cloud_next_image = Image.load_from_file("palm2-multimodalembedding"
                                        "/image-to-text/image/img_1.png")
cloud_next_image.show()

response = image_qna_model.ask_question(
    image=cloud_next_image,
    question="Explain this image?",
    number_of_results=1,
)

print(response)

response = image_qna_model.ask_question(
    image=cloud_next_image,
    question="Identify 3 vegetables from the image?",
    number_of_results=1,
)
print(response)

