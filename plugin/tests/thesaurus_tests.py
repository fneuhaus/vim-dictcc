import unittest
import urllib.error
from dicts import ThesaurusQuery
from unittest.mock import patch


class ThesaurusTests(unittest.TestCase):

    def test_ThesaurusQuery_has_target_word_property(self):
        q = ThesaurusQuery("foobar")
        self.assertEqual(q.target, "foobar")

    def test_ThesaurusQuery_returns_list_of_translations(self):
        q = ThesaurusQuery("thought")
        translations = q.translations
        self.assertGreaterEqual(len(translations), 1)

    def test_ThesaurusQuery_translations_list_is_empty_for_not_found_word(self):
        q = ThesaurusQuery("aksuldgfhuiaerg")
        self.assertListEqual(q.translations, [])

    @patch("urllib.request.urlopen", side_effect=urllib.error.URLError("dooh"))
    def test_ThesaurusQuery_translations_list_is_empty_if_URLError(self, mock):
        q = ThesaurusQuery("thought")
        try:
            self.assertListEqual(q.translations, [])
        except Exception:
            self.fail("Uncaught Exception occurred!")

    def test_ThesaurusQuery_can_return_as_lines(self):
        q = ThesaurusQuery("but")
        lines = q.as_lines()
        self.assertIn("although", lines[1])
