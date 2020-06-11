import unittest

from test_navigator.test_navigator_utils import get_hello_word, get_world_word, get_phrase


class TestAppPrint(unittest.TestCase):
    def test_hello(self):
        word = get_hello_word()
        self.assertEqual(word, 'hello')

    def test_world(self):
        word = get_world_word()
        self.assertEqual(word, 'world')

    def test_phrase(self):
        phrase = get_phrase()
        self.assertEqual(phrase, 'hello world')
