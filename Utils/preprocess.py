import re  
from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()

def text_preprocess(text):
    text = re.sub('<[^>]*>', '', text) 
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = (re.sub('[\W]+', ' ', text.lower()) + ' ' + ' '.join(emoticons).replace('-', ''))
    return text 

def tokenizer(text):
    return text.split()

def tokenizer_port(text):
    return [porter.stem(word) for word in text.split()]