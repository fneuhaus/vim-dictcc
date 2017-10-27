#!/usr/bin/env python
# encoding: utf-8

import re
import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup


class DictQuery(object):

    QUERY_URL = ""
    QUERY_HEADER = {"user-agent": "Mozilla/5.0 (Linux) Gecko"}
    QUERY_METHOD = "POST"

    def __init__(self, target):
        self._target = target
        self._request = urllib.request.Request(
            self.url,
            self.url_parameters,
            self.QUERY_HEADER,
            method=self.QUERY_METHOD,
        )

    @property
    def header(self):
        return "Translations of \"{}\"".format(self.target)

    @property
    def url(self):
        return self.QUERY_URL

    @property
    def url_parameters(self):
        return urllib.parse.urlencode({}).encode("utf-8")

    @property
    def target(self):
        return self._target

    @property
    def translations(self):
        return self._parse_html()

    @property
    def response(self):
        if not hasattr(self, "_response"):
            try:
                response = urllib.request.urlopen(self._request)
                self._response = response.read().decode("utf-8")
            except urllib.error.HTTPError as e:
                # Some pages return 404, when the word is not in their database
                # for example Thesaurus
                return None
            except urllib.error.URLError as e:
                print("Error during dict request: {}".format(e.reason))
                return None
        return self._response

    def as_lines(self):
        lines = [self.header]
        translations = self.translations
        if translations and type(translations[0]) == tuple:
            for i, (left, right) in enumerate(translations):
                line = "{:>2}: {:<35} {}".format(i, left[:35], right[:35])
                lines.append(line)
        else:
            for i, word in enumerate(translations):
                line = "{:>2}: {}".format(i, word)
                lines.append(line)

        return lines

    def _parse_html(self):
        translations = list()

        if self.response is None:
            return translations

        return translations
