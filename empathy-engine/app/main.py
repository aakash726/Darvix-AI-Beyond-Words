from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware  # ✅ ADD THIS
from .tts_service import synthesize

app = FastAPI()

# ✅ Enable CORS (allows your HTML file to call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (or use ["http://127.0.0.1:5500"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Darvix Empathy Engine is running"}

@app.post("/tts")
async def tts_endpoint(text: str = Query(..., description="Text to convert into speech")):
    output_file = await synthesize(text)
    return FileResponse(output_file, media_type="audio/mpeg", filename="output.mp3")
