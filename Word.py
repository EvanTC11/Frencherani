class Word:
    def __init__(self, english : list[str], french : str):
        self.__french = french
        self.__english = english

    def getFrench(self):    return self.__french    
    def getEnglish(self):	return self.__english