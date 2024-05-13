from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")



import requests
import json
url = "https://api.edenai.run/v2/text/syntax_analysis"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTVlYjI0NTktN2FhMi00MjQxLThkN2MtMmE2NWFlMjkxNmRlIiwidHlwZSI6ImFwaV90b2tlbiJ9.hnR156RVg2I6LRwwfO4BShrSCK0demW0dVHSv-su3_8"  # Replace YOUR_API_KEY with your actual API key
}





class API:
    def __init__(self,):
        pass
    def sentimental_analyis(selfs,text):
        sentiment = SentimentIntensityAnalyzer()
        response= sentiment.polarity_scores(text)
        return response

    def ner(self,text):
        text1 = NER(text)
        x=[]
        for word in text1.ents:
            y= f"{word.text}- {word.label_}"
            x.append(y)
        return x





    def syntax_analysis(self,text):
        payload = {
            "providers": "google,amazon",
            "language": "en",
            "text": text
        }
        response = requests.post(url, json=payload, headers=headers)
        result = json.loads(response.text)
        simplified_result = {}
        for provider, data in result.items():
            if 'items' in data:
                items = data['items']
                simplified_result.update({item['word']: item['tag'] for item in items})
        recognized_entity = ""
        for word, tag in simplified_result.items():
            recognized_entity=recognized_entity+f"{word}-{tag}\n"
        return recognized_entity



