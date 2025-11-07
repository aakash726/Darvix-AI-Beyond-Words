import edge_tts

VOICE = "en-US-JennyNeural"

async def synthesize(text: str, file_path: str = "output.mp3") -> str:
    tts = edge_tts.Communicate(text=text, voice=VOICE)
    await tts.save(file_path)
    return file_path
