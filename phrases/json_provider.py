import json
from typing import List
from phrases.interfaces import PhraseProvider

class JsonPhraseProvider(PhraseProvider):
    def __init__(self, filepath: str):
        self._filepath = filepath

    def load_phrases(self) -> List[str]:
        with open(self._filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('phrases', [])
