from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

FAQ_SERVICE_URL = "http://faq-service:8001"
SUMMARIZER_SERVICE_URL = "http://summarizer-service:8002"

@app.post("/ask")
async def ask_openai(prompt: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{FAQ_SERVICE_URL}/ask_openai", json={"prompt": prompt})
            return response.json()
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"FAQ Service Error: {str(e)}")

@app.post("/summarize")
async def summarize(content: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{SUMMARIZER_SERVICE_URL}/summarize", json={"content": content})
            return response.json()
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Summarizer Service Error: {str(e)}")
