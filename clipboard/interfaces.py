from abc import ABC, abstractmethod

class ClipboardManager(ABC):
    @abstractmethod
    def copy(self, text: str) -> None:
        """Copy text to the OS clipboard."""
        ...
