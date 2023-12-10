import time
# import threading
import words as w

class Translator:
    def __init__(self):
        self.words = w.Words()
        self.words.load() # load the words from json file first
        self.wordsArray = self.words.words
        self.text = ""
        self.userInput = ""
        self.translatedWord = ""
        # self.checkWordThread = threading.Thread(target=self.__CheckWord)
        # self.loadingThread = threading.Thread(target=self.__FrencheraniLoop)

    def __GetFrench(self):
        for word in self.wordsArray:
            if self.userInput in word.getEnglish():
                return word.getFrench()
    def __FrencheraniLoop(self):
        for i in range(2):
            print(f"frencherani est working{self.text}")
            self.text += "."
            time.sleep(0.5)

    def __CheckWord(self):
        checkWord = self.words.checkForWord(self.userInput)
        if checkWord:   self.translatedWord = self.__GetFrench()
        else:   self.translatedWord = "invalid input"

    def Run(self):
        self.userInput = input("Pick a word to get (in English): ")
        self.userInput.lower()

        self.__FrencheraniLoop()
        self.__CheckWord()

        # self.checkWordThread.join()
        print(self.translatedWord)

if __name__ == "__main__":
    main = Translator()
    main.Run()