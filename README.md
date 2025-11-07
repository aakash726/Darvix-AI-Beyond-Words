# Empathy Engine (Darvix AI Hackathon Project)

Empathy Engine is a prototype that converts text into speech and changes the tone of voice based on the sentiment of the text. The emotion of the text is detected using a sentiment analysis model, and then the speech is generated using Edge-TTS with a matching voice style.

## Tech Stack
- Backend: FastAPI (Python), HuggingFace Transformers (DistilBERT), Edge-TTS
- Frontend: HTML and JavaScript

## How to Run Locally

```bash
# 1. Create a virtual environment
python -m venv darvix

# 2. Activate the virtual environment (Windows)
darvix\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the FastAPI server
uvicorn app.main:app --reload --port 8001

# 5. Open the browser
# Go to the following URL:
http://localhost:8001
