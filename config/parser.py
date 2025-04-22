import re
from typing import Dict

class ConfigParser:
    """
    Reads a simple config file where each line defines a hotkey→phrase mapping:
      setphrase: "<hotkey>", "<phrase>"
    Blank lines and lines starting with '#' are ignored.
    """

    LINE_RE = re.compile(r'''
        ^\s*setphrase:\s*            # literal "setphrase:"
        "(?P<hotkey>[^"]+)"\s*,\s*   # "hotkey",
        "(?P<phrase>[^"]+)"\s*       # "phrase"
        (?:\#.*)?$                   # optional comment (escaped '#')
    ''', re.IGNORECASE | re.VERBOSE)

    def __init__(self, filepath: str):
        self._filepath = filepath

    def parse(self) -> Dict[str, str]:
        """
        :return: mapping of hotkey string → phrase string
        :raises ValueError: on invalid line syntax
        """
        mapping: Dict[str, str] = {}
        with open(self._filepath, 'r', encoding='utf-8') as f:
            for lineno, raw in enumerate(f, start=1):
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                m = self.LINE_RE.match(line)
                if not m:
                    raise ValueError(
                        f"Invalid config at {self._filepath}:{lineno}: {raw!r}"
                    )
                mapping[m.group('hotkey')] = m.group('phrase')
        return mapping

