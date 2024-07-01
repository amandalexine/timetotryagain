from pyscript import document
import random

def sampleFunc(event) :
    lyrics = ["You've got that one thing", "That's what makes you beautiful", 
              "Nobody can drag me down", "If you ever feel alone, don't", 
              "I wanna live while we're young", "Everything you do is magic",
              "Nobody compares to you"]

    print(random.choice(lyrics))

thisButton = document.querySelector("#press")
thisButton.onclick = sampleFunc