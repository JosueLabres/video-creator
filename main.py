from robots.text import TextRobot
from robots.userInput import UserInput
class Start():
    def __init__(self):
        
        self.searchTerm = UserInput.asKAndReturnSearchTerm()
        self.prefix = UserInput.asKAndReturnPrefix()
        
        textRobot = TextRobot(self.searchTerm)
        self.wikipediaContent = textRobot.fetchContentFromWikipedia()
        self.sanitizeContent = textRobot.sanitizeContent()
        self.sentences = textRobot.breakContentIntoSentences(self.sanitizeContent)
        
    
    def get_content(self):
        return {
            "search_term": self.searchTerm,
            "prefix": self.prefix,
            "wikipedia_content": self.wikipediaContent,
            "sanitizeContent": self.sanitizeContent,
            "sentences": self.sentences
        }

semtemces = Start().sentences

for semtemce in semtemces:
    print(f'{semtemce}\n\n')
