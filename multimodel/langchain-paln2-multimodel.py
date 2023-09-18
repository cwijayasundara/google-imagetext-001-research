import vertexai
from google.cloud import aiplatform


PROJECT_ID = "ibm-keras"
REGION = "us-central1"

aiplatform.init(
    project=PROJECT_ID,
    location=REGION
)
vertexai.init(
    project=PROJECT_ID,
    location=REGION
)

