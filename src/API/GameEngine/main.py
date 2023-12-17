import time
import words as w
import random

class Game:
    def __init__(self):
        self.words = w.Words()
        # self.words.load() load the words from json file first, however in API, we're going to start with an empty array
        self.wordsArray = []
        self.text = ""
        self.userInput = ""
        self.response = ""
        self.running = False

    def __GetFrench(self):
        for word in self.wordsArray:
            if self.userInput in word.getEnglish():
                return word.getFrench()

    def __handleInput(self):
        if self.userInput == "exit":
            self.running = False
        else:
            checkWord = self.words.checkForWord(self.userInput)
            if checkWord:
                self.response = f"Well done! correct!"
            else:
                self.response = f"Incorrect! The correct answer was {self.newWord.getEnglish()[0]}"

    def __chooseWord(self):
        # Pick a random index
        i = random.randint(0, len(self.wordsArray) - 1)
        return self.wordsArray[i]

    def Run(self):
        self.running = True

        while self.running:
            self.newWord = self.__chooseWord()

            self.userInput = input(f"What is {self.newWord.getFrench()} in English? ")
            self.userInput.lower()

            self.__handleInput()
            print(self.response)

if __name__ == "__main__":
    main = Game()
    main.Run()