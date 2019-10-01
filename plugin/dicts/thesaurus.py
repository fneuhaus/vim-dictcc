#!/usr/bin/env python
# encoding: utf-8

import re
import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from .base import DictQuery


class ThesaurusQuery(DictQuery):

    QUERY_URL = "http://www.thesaurus.com/browse/"
    QUERY_METHOD = "GET"

    @property
    def header(self):
        return "Synonyms for \"{}\" from thesaurus.com".format(self.target)

    @property
    def url(self):
        return urllib.parse.urljoin(self.QUERY_URL, self.target)

    @property
    def url_parameters(self):
        return urllib.parse.urlencode({"s": "t"}).encode("utf-8")

    def _parse_html(self):
        translations = list()

        if self.response is None:
            return translations

        soup = BeautifulSoup(self.response, "html.parser")

        re_relevance = re.compile(r"relevance-([0-9]+)")
        def parse_a(a):
            m = re_relevance.search(a.get("data-category", ""))
            relevance = int(m.group(1)) if m else 0
            try:
                text = a.find(class_="text").text
                return (text, relevance)
            except AttributeError:
                return None

        translations_meta = list()
        synonyms_label = soup.find_all(text=re.compile('Synonyms for '))
        if len(synonyms_label) == 0:
            return []
        links = synonyms_label[0].parent.parent.select('ul li>span')
        if links:
            entries = len(links)
            for i, a in enumerate(links):
                res = (a.text, entries - i)
                if res:
                    translations_meta.append(res)
        translations = [w[0] for w in sorted(translations_meta, key=lambda x: -x[1])]

        return translations
