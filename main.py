from Head.Mouth import *
from Head.Ear import *
from Head.brain import *
from Function.wish import wish

def assistant():
    wish()
    while True:
        text = listen().lower()
        brain(text)
        # text = mind(text)
        # speak(text)


assistant()
