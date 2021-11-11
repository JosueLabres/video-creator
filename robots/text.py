import requests
from bs4 import BeautifulSoup
import pysbd
class TextRobot():
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm
        self.wikipedia = ''
    def fetchContentFromWikipedia(self):
       r = requests.get(f'https://pt.wikipedia.org/wiki/{self.searchTerm}')
       bs = BeautifulSoup(r.text, 'html.parser')
       content = bs.find(id='mw-content-text')
       content = content.find_all('p')
       wikipedia = ''
       for p in content:
           wikipedia = f'{wikipedia}{p.get_text()}'
       self.wikipedia = wikipedia
       return wikipedia
    def sanitizeContent(self):
        ...
    
    def breakContentIntoSentences(self):
        seg = pysbd.Segmenter(language="en", clean=False)
        return seg.segment(self.wikipedia)