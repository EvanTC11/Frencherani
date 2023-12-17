import json
import word

class Words:
    def __init__(self, filepath="words.json"):
        self.words = []
        self.filePath = filepath

    def load(self):
        with open(self.filePath, "r") as self.file: self.roomsDic = json.load(self.file)
        self.key = self.roomsDic["words"]
        for i in range(len(self.key)):
            self.loopKey = self.key[i]
            self.words.append(word.Word(self.loopKey["english"], self.loopKey["french"]))

    def checkForWord(self, wordToCheck : str):
        for i in range(len(self.words)):
            wordsArray = self.words[i].getEnglish()
            for x in range(len(wordsArray)):
                if wordToCheck in wordsArray[x].lower():   return True

        return False