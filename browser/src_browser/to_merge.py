from pyscript import document

# Variables
input_box = document.querySelector("#input")
output_div = document.querySelector("#output")
inputButtonPressed = False
global inputButtonPressed

# Handlers for input, output, and buttonDetection
def handleInput(prefix):
    input_box.placeholder = str(prefix)
    while not inputButtonPressed:
        pass
    inputButtonPressed = False
    return str(input_box.value)
def handleOutput(text):
    output_box.innerText = output_box.innerText + text
def triggerInputSubmition():
    inputButtonPressed = True

