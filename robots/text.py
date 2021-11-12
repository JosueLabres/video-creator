import requests
from bs4 import BeautifulSoup
import pysbd
import re
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1  import Features, EntitiesOptions, KeywordsOptions
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
    
    
    def watson(self,sentences, maxSentences):
        sentence = []
        for i in range(maxSentences):
            print('get watson')
            
            natural_language_understanding = NaturalLanguageUnderstandingV1(
                version='2021-08-01',
                
            )
            response = natural_language_understanding.analyze(
                text=sentences[i],
                features=Features(keywords=KeywordsOptions())).get_result()
            keywords = []
            for keyword in response['keywords']:
                keywords.append(keyword['text'])
            sentence.append({
                'sentence': sentences[i],
                'keywords': keywords
            })
        return sentence
        
