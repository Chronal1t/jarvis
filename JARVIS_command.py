import os
import webbrowser
import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
import time

stemmer = SnowballStemmer("russian")


def choose_command(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in tokens]
    stemmed_text = ' '.join(stemmed_words)
    

command = {
    
}