import vertexai
import os
import requests

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


def download_image(url):
    """Downloads an image from the specified URL."""

    # Send a get request to the url
    response = requests.get(url)

    # If the request is successful
    if response.status_code == 200:

        # Define image related variables
        image_path = os.path.basename(url)
        image_bytes = response.content
        image_type = response.headers['Content-Type'].split('/')[1]

        # Check for image type, currently only PNG or JPEG format are supported
        if image_type in ("png", "jpg", "jpeg"):

            # Write image data to a file
            with open(image_path, "wb") as f:
                f.write(image_bytes)
            return image_path
        else:
            raise Exception("Image can only be in PNG or JPEG format")

    else:
        raise Exception(f"Failed to download image from {url}")

# Download an image
url = "https://storage.googleapis.com/gweb-cloudblog-publish/images/GettyImages-871168786.max-2600x2600.jpg"
image_path = download_image(url)

# Load the newly downloaded image
user_image = Image.load_from_file(image_path)
user_image.show()

response = image_qna_model.ask_question(
    image=user_image,
    question="What is happening in this photo?",
    number_of_results=3,
)

print(response)

response = image_qna_model.ask_question(
    image=user_image,
    question="What advertising channels would this image be suitable for?",
    number_of_results=3,
)

print(response)

response = image_qna_model.ask_question(
      image=user_image,
      question="What type of insects could live in this area?",
      number_of_results=3,
)

print(response)
