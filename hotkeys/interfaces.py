from abc import ABC, abstractmethod

class HotkeyHandler(ABC):
    @abstractmethod
    def start_listening(self) -> None:
        """Begin listening for configured hotkeys."""
        ...
