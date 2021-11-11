from robots.text import TextRobot
from robots.userInput import UserInput
class Start():
    def __init__(self):
        
        self.searchTerm = UserInput.asKAndReturnSearchTerm()
        self.prefix = UserInput.asKAndReturnPrefix()
        
        textRobot = TextRobot(self.searchTerm)
        self.wikipediaContent = textRobot.fetchContentFromWikipedia()
        self.sentences = textRobot.breakContentIntoSentences()
    
    def get_content(self):
        return {
            "search_term": self.searchTerm,
            "prefix": self.prefix,
            "wikipedia_content": self.wikipediaContent,
            "sentences": self.sentences
        }

print(Start().get_content())
