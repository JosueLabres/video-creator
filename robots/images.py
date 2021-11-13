import json
import requests
class ImageRobot():
    def __init__(self):
        with open('googleCredentials.json', 'r', encoding='utf8') as f:
            credentials =  json.load(f) 
            self.api_key = credentials['custonsearch']['api_key']
            self.cx = credentials['custonsearch']['cx']
        with open('data.json', 'r', encoding='utf8') as f:
            self.content = json.load(f) 
            
        
    def searchImageOfSentences(self):
        sentences = self.content['sentences']
        imageSentences = []
        for sentence in sentences:
            keywords = sentence['keywords']
            images = self.fetchGoogleAndReturnImagesLink(f'{self.content["search_term"]} {keywords[0]}')
            imageSentences.append({
                "sentence": sentence['sentence'],
                "keywords": sentence['keywords'],
                "googleSearchQuery": f'{self.content["search_term"]} {keywords[0]}',
                "images": images
            })
        
        self.content['sentences'] = imageSentences
        
        return self.content
    
    def fetchGoogleAndReturnImagesLink(self,query):  
        r = requests.get(f'https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.cx}&q={query}&searchType=image&num=4').json()
        
        imagesUrl = []
        for item in r['items']:
            imagesUrl.append(item['link'])
        
        return imagesUrl
        
        
        
