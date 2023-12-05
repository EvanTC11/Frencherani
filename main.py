import time
import words as w

words = w.words

text = ""

userInput = input("Pick a word to get (in English): ")
userInput.lower()

def getAns(usrInput : str):
    for i in range(len(words)):
        if usrInput == words[i].getEnglish():
            return words[i].getFrench()

for i in range(5):
    print(f"frencherani est working{text}")
    text += "."
    time.sleep(1)

if w.CheckForWord(userInput):
    print(getAns(userInput))

else:
    print("invalid input")