# Vectex AI hackathon

## Summary

Using vector store with vertex ai to generate fact based conversation

## How to start

Go to the link: https://vectorstore-chatbot.vercel.app/
With the front end here: https://github.com/FengJi2021/vectorstore-chatbot

Fastapi is deployed on GCP VM.

### Clone and install dependencies

In your terminal, run the following commands:

```
cd app
pip install -r requirements.txt
```

### Update the project auth

In order to use the Vertex AI SDK, you will need to update the project auth using a serviceaccount

In `app`, folder create the file `service_account.json` and paste the content of your service account json file. Create the file if you don't have it by runnung the following command in your terminal:

`touch service_account.json`

In the file `service_account.json` paste the content of your service account json file. It should look like this:

```
{
    "type": "service_account",
    "project_id": "YOUR_PROJECT_ID",
    "private_key_id": "YOUR_PRIVATE_KEY_ID",
    "private_key": "YOUR_PRIVATE_KEY",
    "client_email": "YOUR_CLIENT_EMAIL",
    "client_id": "YOUR_CLIENT_ID",
    "auth_uri": "YOUR_AUTH_URI",
    "token_uri": "YOUR_TOKEN_URI",
    "auth_provider_x509_cert_url": "YOUR_AUTH_PROVIDER_X509_CERT_URL",
    "client_x509_cert_url": "YOUR_CLIENT_X509_CERT_URL",
    "universe_domain": "YOUR_UNIVERSE_DOMAIN"
}
```

You can find your service account json file in the Vertex AI console under `Settings > Service account` or you got it provided by lablab.ai (If you are part of the Google Vertex AI hackathon )

### Start the server and test

Once you have installed the dependencies, you can start the server by running: `uvicorn main:app --reload --port 8080` in the `app` directory.
When the server is running, you can test it by going to `http://localhost:8080/docs` in your browser. You should see the Swagger UI where you can test the endpoints.

![image](https://github.com/lablab-ai/Google-VertexAI-FastAPI/assets/2171273/13df1172-0b77-43f3-85a0-0bf936bbd8db)
![image](https://github.com/lablab-ai/Google-VertexAI-FastAPI/assets/2171273/e69f7892-6945-4d85-987e-dbbc23e553bd)
