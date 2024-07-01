from pyscript import document

def sampleFunc(event) :
  print("You've got that one thing!")

thisButton = document.querySelector("#press")
thisButton.onclick = sampleFunc