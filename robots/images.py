import json
import requests
from download import download
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
    
    def downloadImages():
         with open('data.json', 'r', encoding='utf8') as f:
            content = json.load(f)
            sentences = content['sentences'] 
            
            for i in range(len(sentences)):
                imagensBaixadas = []
                links = sentences[i]['images']
                
                for link in links:
                    try:
                        if link in imagensBaixadas:
                            raise Exception('imagem ja baixada')
                        if 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com' in link:
                            raise Exception('dominio bloqueado')
                        path = download(link, f'images/{i}-original.png', replace=True)
                        break
                    except Exception as e:
                        print(f'Erro ao baixar: {e}')
                
                
ImageRobot.downloadImages()
        
        
