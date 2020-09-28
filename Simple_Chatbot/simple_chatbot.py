# Simple Chatbot using python (No GUI)

# Importing the Libraries
from nltk.chat.util import Chat, reflections

# creating user input and it's respective response list
pairs = [
    ['hello|hi|hey', ['Hello', 'Hey There']],
    ['my name is (.*)', ['Hi %1, how are you today']],
    ['what is your name(.*)', ['I am GovNaB :)']],
    ['how are you(.*)', ['I am fine, How about you ?']],
    ['fine(.*)|i am fine(.*)|great|doing great', ['Nice to hear :o']],
    ['age(.*)|your age(.*)|what is your age(.*)|how old are you(.*)', ['Asking someone\'s age is a rude step towards them :(']],
    ['sorry(.*)', ['It\'s Okay, never mind :)']],
    ['who is your creator(.*)|who created you(.*)|who made you(.*)', ['Yashasvi Bhatt created me using NLTK Library of Python']],
    ['quit', ['Bye! Take Care']]
]

print('Hello there! Please enter small case letters to chat with me, or enter quit to leave')

chat = Chat(pairs, reflections)                         # binding the input and their respective response
chat.converse()                                         # taking input from user and printing it's respective response