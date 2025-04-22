from abc import ABC, abstractmethod
from typing import List

class PhraseProvider(ABC):
    @abstractmethod
    def load_phrases(self) -> List[str]:
        """Return all saved phrases."""
        ...
