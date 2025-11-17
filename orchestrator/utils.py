
import json
def safe_parse_jsonish(text: str):
    try:
        return json.loads(text)
    except Exception:
        return text
