import time
import threading
import words as w

class Translator:
    def __init__(self):
        self.words = w.words
        self.text = ""
        self.userInput = ""
        self.translatedWord = ""
        self.checkWordThread = threading.Thread(target=self.__CheckWord)
        self.loadingThread = threading.Thread(target=self.__FrencheraniLoop)

    def __GetAns(self, usrInput : str):
        for i in range(len(self.words)):
            currentWords = self.words[i].getEnglish()
            for x in range(len(currentWords)):
                if usrInput == currentWords[x]:
                    return self.words[i].getFrench()
                
    def __FrencheraniLoop(self):
        while self.checkWordThread.is_alive():
            print(f"frencherani est working{self.text}")
            self.text += "."
            time.sleep(0.5)

    def __CheckWord(self):
        if w.CheckForWord(self.userInput):
            self.translatedWord = self.__GetAns(self.userInput)
        else:
            print("invalid input")
            
        time.sleep(1)

    def Run(self):
        self.userInput = input("Pick a word to get (in English): ")
        self.userInput.lower()

        self.checkWordThread.start()
        self.loadingThread.start()
        self.checkWordThread.join()
        print(self.translatedWord)

if __name__ == "__main__":
    main = Translator()
    main.Run()