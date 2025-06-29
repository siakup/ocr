from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import pytesseract, requests, io, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # atau ["*"] untuk bebas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ocr")
async def ocr(image: UploadFile = File(...)):
    img_bytes = await image.read()
    img = Image.open(io.BytesIO(img_bytes))
    text = pytesseract.image_to_string(img)

    # Kirim ke Ollama (DeepSeek)
    # res = requests.post(
    #     "http://localhost:11434/api/generate", 
    #     json={
    #         "model": "deepseek-r1:14b",  # atau model kamu
    #         "prompt": f"Ringkas teks berikut:\n{text}",
    #         "stream": False
    #     }, 
    #     # timeout=120
    # )

    # if res.status_code != 200:
    #     raise HTTPException(status_code=502, detail="Ollama error")

    # res.raise_for_status()          # error handling
    # result = res.json()             # sekarang pasti JSON utuh

    return {
        "ocr_text": text, 
        # "llm_response": result.get("response", "")
    }
