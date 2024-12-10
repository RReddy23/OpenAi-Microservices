from fastapi import FastAPI, HTTPException
import os
# from openai import OpenAIClient
# from azure.core.credentials import AzureKeyCredential

from openai import AzureOpenAI
    


app = FastAPI()

# Load environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
DEPLOYED_MODEL = os.getenv("DEPLOYED_MODEL")

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,  
    api_version=DEPLOYED_MODEL,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# Initialize OpenAI Client
# client = OpenAIClient(endpoint=AZURE_OPENAI_ENDPOINT, credential=AzureKeyCredential(AZURE_OPENAI_API_KEY))


@app.post("/summarize")
async def summarize(content: str):
    try:
        response = client.chat_completions.create(
            deployment_id=DEPLOYED_MODEL,
            messages=[{"role": "user", "content": f"Summarize this: {content}"}],
        )
        return {"summary": response.choices[0].message["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
