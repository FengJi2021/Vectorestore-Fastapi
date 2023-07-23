import json  # add this line

import google.cloud.aiplatform as aiplatform
import vertexai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from google.oauth2 import service_account
from vector_qa import VectorQA
from vertexai.preview.language_models import ChatModel

# Load the service account json file
# Update the values in the json file with your own
CRED_PATH = "../cred/service_account.json"
with open(CRED_PATH) as f:
    service_account_info = json.load(f)

my_credentials = service_account.Credentials.from_service_account_info(
    service_account_info
)

# Initialize Google AI Platform with project details and credentials
aiplatform.init(
    credentials=my_credentials,
)

with open(CRED_PATH, encoding="utf-8") as f:
    project_json = json.load(f)
    project_id = project_json["project_id"]


# Initialize Vertex AI with project and location
vertexai.init(project=project_id, location="us-central1")

# Initialize the FastAPI application
app = FastAPI()

# Configure CORS for the application
origins = ["http://localhost", "http://localhost:8080", "http://localhost:3000"]
origin_regex = r"https://(.*\.)?alexsystems\.ai"
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=origin_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint that returns available endpoints in the application"""
    return {
        "Endpoints": {
            "chat": "/chat",
        }
    }


@app.get("/docs")
async def get_documentation():
    """Endpoint to serve Swagger UI for API documentation"""
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.post("/chat")
async def handle_chat(human_msg: str):
    """
    Endpoint to handle chat.
    Receives a message from the user, processes it
    and returns a response from the model.
    """
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "temperature": 0.8,
        "max_output_tokens": 1024,
        "top_p": 0.8,
        "top_k": 40,
    }
    chat = chat_model.start_chat(  # Initialize the chat with model
        # chat context and examples go here
    )
    # Send the human message to the model and get a response
    response = chat.send_message(human_msg, **parameters)
    # Return the model's response
    return {"response": response.text}


langchain_qa = VectorQA()


@app.post("/embedding")
async def handle_question(msg: str):
    """
    Endpoint to handle incoming questions.
    """
    response = langchain_qa.process(msg)
    return {"response": "Answer: " + response + "\n"}
