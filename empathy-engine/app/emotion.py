from typing import Tuple

try:
    from transformers import pipeline
    _pipeline = pipeline('sentiment-analysis')
except Exception:
    _pipeline = None


def detect_emotion(text: str) -> Tuple[str, float]:
    text = text.strip()
    if not text:
        return 'neutral', 0.0

    if _pipeline:
        try:
            out = _pipeline(text, truncation=True)[0]
            label = out.get('label', '').lower()
            score = float(out.get('score', 0.0))

            if 'positive' in label:
                return 'positive', score
            if 'negative' in label:
                return 'negative', score
            return 'neutral', score

        except Exception:
            pass

    positive_words = set(["good", "great", "awesome", "happy", "love", "excellent", "fantastic", "amazing", "best"])
    negative_words = set(["bad", "terrible", "awful", "hate", "sad", "angry", "worst", "disappoint", "frustrat"])

    t = text.lower()
    pos_count = sum(1 for w in positive_words if w in t)
    neg_count = sum(1 for w in negative_words if w in t)

    if pos_count == neg_count:
        return 'neutral', 0.6
    if pos_count > neg_count:
        return 'positive', min(0.9, 0.5 + 0.2 * pos_count)
    return 'negative', min(0.9, 0.5 + 0.2 * neg_count)
