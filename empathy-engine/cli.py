import argparse
from app.emotion import detect_emotion
from app.tts_service import synthesize


parser = argparse.ArgumentParser()
parser.add_argument('--text', '-t', required=True)
parser.add_argument('--out', '-o', default='out.wav')
args = parser.parse_args()


label, score = detect_emotion(args.text)
print('Detected:', label, 'score:', score)
synthesize(args.text, label, score, args.out)
print('Saved to', args.out)