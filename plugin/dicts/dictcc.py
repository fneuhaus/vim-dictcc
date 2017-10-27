#!/usr/bin/env python
# encoding: utf-8

import re
import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from .base import DictQuery


class DictCCQuery(DictQuery):

    QUERY_URL = "https://www.dict.cc"

    @property
    def header(self):
        return "Translations of \"{}\" from dict.cc".format(self.target)

    @property
    def url_parameters(self):
        return urllib.parse.urlencode({"s": self.target}).encode("utf-8")

    def _parse_html(self):
        translations = list()

        if self.response is None:
            return translations

        soup = BeautifulSoup(self.response, "html.parser")

        def parse_table_col(td):
            w = str()
            for a in td.find_all("a"):
                w += " {}".format(a.text)
            return w.strip()

        # table rows containing translations are numbered tr[0-9]+
        for tr in soup.find_all("tr", {"id": re.compile("tr*")}):
            td_left, td_right = tr.find_all("td")[1:3]
            translations.append(
                (parse_table_col(td_left), parse_table_col(td_right)))

        return translations
