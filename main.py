from robots.text import TextRobot
from robots.userInput import UserInput
class Start():
    def __init__(self):
        maxSentences = 7
        self.searchTerm = UserInput.asKAndReturnSearchTerm()
        self.prefix = UserInput.asKAndReturnPrefix()
        
        textRobot = TextRobot(self.searchTerm)
        self.wikipediaContent = textRobot.fetchContentFromWikipedia()
        self.sanitizeContent = textRobot.sanitizeContent()
        sentences = textRobot.breakContentIntoSentences(self.sanitizeContent)
        self.sentences = textRobot.watson(sentences, maxSentences)
    
    def get_content(self):
        return {
            "search_term": self.searchTerm,
            "prefix": self.prefix,
            "wikipedia_content": self.wikipediaContent,
            "sanitizeContent": self.sanitizeContent,
            "sentences": self.sentences
        }



print(Start().sentences)