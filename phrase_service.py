from typing import List
from phrases.interfaces import PhraseProvider
from clipboard.interfaces import ClipboardManager

class PhraseService:
    def __init__(self, provider: PhraseProvider, clipboard: ClipboardManager):
        self._provider = provider
        self._clipboard = clipboard

    def copy_phrase(self, index: int) -> None:
        """Load phrases and copy the selected one to the clipboard."""
        phrases: List[str] = self._provider.load_phrases()
        if 0 <= index < len(phrases):
            self._clipboard.copy(phrases[index])
