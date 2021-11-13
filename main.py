from json import encoder

from requests.models import encode_multipart_formdata
from robots.text import TextRobot
from robots.userInput import UserInput
import json
class Start():
    def __init__(self):
        maxSentences = 1
        self.searchTerm = UserInput.asKAndReturnSearchTerm()
        self.prefix = UserInput.asKAndReturnPrefix()
        
        textRobot = TextRobot(self.searchTerm)
        self.wikipediaContent = textRobot.fetchContentFromWikipedia()
        self.sanitizeContent = textRobot.sanitizeContent()
        sentences = textRobot.breakContentIntoSentences(self.sanitizeContent)
        self.sentences = textRobot.watson(sentences, maxSentences)
    
    def get_content(self):
        content =  {
            "search_term": self.searchTerm,
            "prefix": self.prefix,
            "wikipedia_content": self.wikipediaContent,
            "sanitizeContent": self.sanitizeContent,
            "sentences": self.sentences
        }
        
        with open('data.json', 'w') as outfile:
            json.dump(content, outfile )
            
        return content
        



print(Start().get_content())