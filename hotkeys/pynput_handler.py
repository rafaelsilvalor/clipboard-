from hotkeys.interfaces import HotkeyHandler
from pynput import keyboard
from typing import Callable, Dict

class PynputHotkeyHandler(HotkeyHandler):
    def __init__(self, hotkey_actions: Dict[str, Callable[[], None]]):
        """
        :param hotkey_actions: mapping from a hotkey spec (e.g. '<alt>+1') to a
                              zero‑arg callable to run when that hotkey fires.
        """
        self._hotkey_actions = hotkey_actions

    def start_listening(self) -> None:
        """Begin listening for the configured hotkeys indefinitely."""
        with keyboard.GlobalHotKeys(self._hotkey_actions) as listener:
            listener.join()
