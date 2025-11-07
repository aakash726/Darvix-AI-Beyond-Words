Empathy Engine (Darvix AI Hackathon Project)

Empathy Engine is a prototype that converts text into speech and changes the tone of voice based on the sentiment of the text. The emotion of the text is detected using a sentiment analysis model, and then the speech is generated using Edge-TTS with a matching voice style.

Tech Stack:
Backend: FastAPI (Python), HuggingFace Transformers (DistilBERT), Edge-TTS
Frontend: HTML and JavaScript

How to run:

Create a virtual environment:
python -m venv darvix

Activate the environment:
Windows:
darvix\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Start the server:
uvicorn app.main:app --reload --port 8001

Open the browser:
http://localhost:8001