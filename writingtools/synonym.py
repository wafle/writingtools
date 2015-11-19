import itertools

__author__ = 'wafle'
from requests_futures.sessions import FuturesSession
import json
from bs4 import BeautifulSoup


def synonyms(word):
    page = FuturesSession().get("http://www.thesaurus.com/browse/{}".format(word)).result().text
    soup = BeautifulSoup(page, "html.parser")
    links = (synonym_li for synonym_li in soup.find(id="synonyms-0").find(class_="relevancy-block").find_all("a"))
    for relevance, (key, group) in enumerate(itertools.groupby(links, key=lambda link: link["data-category"])):
        words = list(link.find(class_="text").text.strip() for link in group)
        print("{} : {}".format(relevance+1, ", ".join(words)))
        
def main():
    import sys
    arguments = sys.argv[1:]
    if len(arguments) == 1:
        synonyms(arguments[0])
    else:
        print("usage: synonym <word>")
