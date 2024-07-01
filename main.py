from pyscript import document
import random

def sampleFunc(event) :
    lyrics = ["You've got that one thing", "That's what makes you beautiful", 
              "Nobody can drag me down", "If you ever feel alone, don't", 
              "I wanna live while we're young", "Everything you do is magic",
              "Nobody compares to you", "You're insecure",
              "You and me got a whole lot of history",
              "I can make your tears fall down like the showers that are British",
              "The story of my life", "Even when the night changes, it'll never change me and you",
              "It's gotta be you", "Reality ruined my life",
              "We're like 'Na na na,' then we're like 'Yeah yeah yeah'",
              "Baby I'm perfect for you", "You make me strong",
              "I speak a different language, but I still hear you call"]

    print(random.choice(lyrics))

thisButton = document.querySelector("#press")
thisButton.onclick = sampleFunc