from config.parser import ConfigParser
from clipboard.windows_clipboard import WindowsClipboardManager
from hotkeys.pynput_handler import PynputHotkeyHandler

def main():
    # 1) Parse your config file
    cfg = ConfigParser('config/phrases.cfg')
    mapping = cfg.parse()  # Dict[str, str]: hotkey → phrase

    # 2) Prepare your clipboard manager
    clipboard = WindowsClipboardManager()

    # 3) Build a hotkey → action mapping
    hotkey_actions = {
        hotkey: (lambda phrase=phrase: clipboard.copy(phrase))
        for hotkey, phrase in mapping.items()
    }

    # 4) Start listening
    hotkey_handler = PynputHotkeyHandler(hotkey_actions)
    hotkey_handler.start_listening()

if __name__ == '__main__':
    main()
