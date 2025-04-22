import unittest
import tempfile
from config.parser import ConfigParser


class TestConfigParser(unittest.TestCase):
    def setUp(self):
        self.sample = """
        # This is a comment
        setphrase: "alt+1", "Hello World"

        setphrase: "ctrl+alt+g", "Good game!"  # inline comment
        """
        self.tf = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.cfg')
        self.tf.write(self.sample)
        self.tf.flush()

    def tearDown(self):
        self.tf.close()

    def test_parse_success(self):
        parser = ConfigParser(self.tf.name)
        mapping = parser.parse()
        self.assertEqual(mapping, {
            'alt+1': 'Hello World',
            'ctrl+alt+g': 'Good game!'
        })

    def test_parse_invalid_line(self):
        # Inject a bad line at the end
        with open(self.tf.name, 'a', encoding='utf-8') as f:
            f.write("\nsetphrase: bad_line_without_quotes\n")
        parser = ConfigParser(self.tf.name)
        with self.assertRaises(ValueError):
            parser.parse()


if __name__ == '__main__':
    unittest.main()
