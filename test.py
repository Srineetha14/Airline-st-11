import re
from string import capwords
import nltk
from nltk.corpus import word_tokenize
from nltk.downloader('punkt')


class Texttonum:
    def __init__(self):
        pass
    def cleaner(self):
        text = re.sub(r',','',self.test)
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        cleaned_text = cleaned_text.strip()
        self.cleaned=cleaned_data
    
    def token(self):
        self.tkns=word_tokenize(self.cleaned)
        
    def removeStop(self):
        stop=stopwords.words('english')
        self.c1 = [i for i in self.tkns if i not in stop]
        
    def stemme(self):
        ps=PorterStemmer()
                        