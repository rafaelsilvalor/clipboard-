import unittest
import tempfile
import json
from phrases.json_provider import JsonPhraseProvider

class TestJsonPhraseProvider(unittest.TestCase):
    def test_load_phrases(self):
        sample = {'phrases': ['hello', 'world']}
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as tf:
            json.dump(sample, tf)
            tf.flush()
            provider = JsonPhraseProvider(tf.name)
            self.assertEqual(provider.load_phrases(), ['hello', 'world'])

if __name__ == '__main__':
    unittest.main()

