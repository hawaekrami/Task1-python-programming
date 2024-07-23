# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 17:43:01 2024

@author: UOD Student
"""


import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import random


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


lemmatizer = WordNetLemmatizer()


greetings = ["Hello!", "Hi there!", "Hey, how's it going?", "Greetings!"]


farewells = ["Goodbye!", "See you later!", "Have a great day!", "Bye bye!"]


def respond(user_input):
    user_input = user_input.lower()
    tokens = nltk.word_tokenize(user_input)
    
    
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.lower() not in stopwords.words('english')]
    
    
    if any(word in tokens for word in ['hello', 'hi', 'hey']):
        return random.choice(greetings)
    
    
    elif any(word in tokens for word in ['goodbye', 'bye', 'see you']):
        return random.choice(farewells)
    
    
    else:
        return "I'm afraid I don't understand. Can you please rephrase your message?"

# Main chatbot loop
print("Welcome to the chatbot! Start chatting (type 'exit' to quit):")

while True:
    user_input = input("> ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    response = respond(user_input)
    print(response)
