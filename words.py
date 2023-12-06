import Word as w
import json
from enum import Enum # enumerator

class WordActions(Enum):
    TRUE = 0,
    CHANGEKEY = 1,
    FALSE = 2

salut = w.Word(["hi"], "salut")
bonjour = w.Word(["hello"], "bonjour")
cava = w.Word(["how are you"], "Ça va")
comment = w.Word(["how", "when"], "comment", True)

words = [salut, bonjour, cava, comment]

fileData = json.load(open("words.json", "r"))

def isChangeAbleKey(word : str):
        # try to identify the first key if multiple meanings
        for i in range(words.__len__()):
            wordArray = words[i].getEnglish()
            for x in range(len(wordArray)):
                if wordArray[x] == word:
                    return True

        return False
                
def changeKey(originalKey : str):
    for i in range(words.__len__()):
        arrayofI = words[i].getEnglish()
        for x in range(len(arrayofI)):
            if arrayofI[x] == originalKey:
                return arrayofI[0]

def CheckForWord(word : str):

    try:
        fileData[word]
        return WordActions.TRUE
    
    except KeyError:
        if isChangeAbleKey(word):   return WordActions.CHANGEKEY
            
    return WordActions.FALSE
