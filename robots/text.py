import requests
from bs4 import BeautifulSoup
import pysbd
import re
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
        sanitize = re.sub('\[[0-9]*\]', ' ', self.wikipedia)
        return sanitize
    
    def breakContentIntoSentences(self, text):
        seg = pysbd.Segmenter(language="en", clean=False)
        return seg.segment(text)