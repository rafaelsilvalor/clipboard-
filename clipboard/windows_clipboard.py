import pyperclip
from clipboard.interfaces import ClipboardManager

class WindowsClipboardManager(ClipboardManager):
    def copy(self, text: str) -> None:
        pyperclip.copy(text)
