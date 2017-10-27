import unittest
import urllib.error
from dicts import DictCCQuery
from unittest.mock import patch


class DictCCTests(unittest.TestCase):

    def test_DictCCQuery_has_target_word_property(self):
        q = DictCCQuery("foobar")
        self.assertEqual(q.target, "foobar")

    def test_DictCCQuery_returns_list_of_translations(self):
        q = DictCCQuery("thought")
        translations = q.translations
        self.assertGreaterEqual(len(translations), 1)

    def test_DictCCQuery_translations_list_is_empty_for_not_found_word(self):
        q = DictCCQuery("aksuldgfhuiaerg")
        self.assertListEqual(q.translations, [])

    @patch("urllib.request.urlopen", side_effect=urllib.error.URLError("dooh"))
    def test_DictCCQuery_translations_list_is_empty_if_URLError(self, mock):
        q = DictCCQuery("thought")
        try:
            self.assertListEqual(q.translations, [])
        except Exception:
            self.fail("Uncaught Exception occurred!")

    def test_DictCCQuery_can_return_as_lines_staring_with_target(self):
        q = DictCCQuery("aber")
        first_line = q.as_lines()[0]
        self.assertIn("aber", first_line)

    def test_DictCCQuery_can_return_as_lines(self):
        q = DictCCQuery("aber")
        lines = q.as_lines()
        self.assertIn("but", lines[1])
        self.assertIn("aber", lines[1])
